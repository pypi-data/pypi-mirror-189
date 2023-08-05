# Copyright (c) Facebook, Inc. and its affiliates. All rights reserved.
#
# This source code is licensed under the BSD license found in the
# LICENSE file in the root directory of this source tree.

import math
from dataclasses import dataclass
from typing import Any, List, Mapping, Optional, Set, Tuple, Type, Union

import torch

from ..._cpp_lib import _built_with_cuda
from ..common import BaseOperator
from .attn_bias import AttentionBias, BlockDiagonalMask, LowerTriangularMask


def _is_bias_type_supported_in_BMK(attn_bias_type: Any) -> bool:
    # NoneType
    if isinstance(None, attn_bias_type):
        return True
    if attn_bias_type in [LowerTriangularMask, torch.Tensor]:
        return True
    return False


@dataclass
class Inputs:
    """
    Stores inputs to the `memory_efficient_attention` operators
    """

    query: torch.Tensor
    key: torch.Tensor
    value: torch.Tensor
    attn_bias: Optional[Union[torch.Tensor, AttentionBias]] = None
    p: float = 0.0
    scale: Optional[float] = None

    @property
    def device(self) -> torch.device:
        return self.query.device

    @property
    def scale_float(self) -> float:
        return self.query.shape[-1] ** (-0.5) if self.scale is None else self.scale

    def normalize_bmhk(self) -> Tuple[int, ...]:
        if self.query.ndim not in [3, 4]:
            raise ValueError(
                f"Invalid shape for query: {self.query.shape}. "
                "Expected shape [batch, seqlen, num_heads, K], or [batch, seqlen, K]."
            )
        output_shape = (self.query.shape[:-1]) + (self.value.shape[-1],)
        # Convert from legacy format
        if self.query.ndim == 3:
            self.query = self.query.unsqueeze(2)
            self.key = self.key.unsqueeze(2)
            self.value = self.value.unsqueeze(2)
        return output_shape

    def validate_inputs(self) -> None:
        qkv = (self.query, self.key, self.value)
        if self.query.ndim not in (3, 4) or any(x.ndim != self.query.ndim for x in qkv):
            raise ValueError(
                f"Query/Key/Value should all have BMHK or BMK shape.\n"
                f"  query.shape: {self.query.shape}\n"
                f"  key.shape  : {self.key.shape}\n"
                f"  value.shape: {self.value.shape}"
            )
        if any(x.device != self.query.device for x in qkv):
            raise ValueError("Query/Key/Value should all be on the same device")
        if any(x.dtype != self.query.dtype for x in qkv):
            raise ValueError(
                "Query/Key/Value should all have the same dtype\n"
                f"  query.dtype: {self.query.dtype}\n"
                f"  key.dtype  : {self.key.dtype}\n"
                f"  value.dtype: {self.value.dtype}"
            )
        # Biases with tensors attached are meant to be in BMHK format
        # This would require to permute biases/gradients which can be expensive,
        # so let's just forbid it - BMK is a legacy format anyway
        if self.query.ndim == 3 and not _is_bias_type_supported_in_BMK(
            type(self.attn_bias)
        ):
            raise ValueError(
                f"Please provide inputs in BMHK format rather "
                f"than BMK when using bias type `{type(self.attn_bias).__name__}`"
            )
        if isinstance(self.attn_bias, BlockDiagonalMask):
            if any(x.shape[0] != 1 for x in qkv):
                raise ValueError(
                    f"Expected batch_size=1 when using block-diagonal bias\n"
                    f"  query.shape: {self.query.shape}\n"
                    f"  key.shape  : {self.key.shape}\n"
                    f"  value.shape: {self.value.shape}"
                )
        if self.p < 0.0 or self.p > 1.0:
            raise ValueError(f"Invalid dropout probability: p={self.p}")


@dataclass
class Context:
    lse: torch.Tensor
    out: torch.Tensor
    op_bw: Optional[Type["AttentionBwOpBase"]] = None
    rng_state: Optional[torch.Tensor] = None

    def get_padded_lse(self, pad_to: int, force_pad_inf: bool = False) -> torch.Tensor:
        pad_amount = (pad_to - (self.lse.shape[2] % pad_to)) % pad_to
        lse = self.lse
        if pad_amount > 0:
            if force_pad_inf:
                lse = lse[:, :, : self.out.shape[1]]
                pad_amount = (pad_to - (lse.shape[2] % pad_to)) % pad_to
            lse = torch.nn.functional.pad(lse, [0, pad_amount], value=math.inf)
        elif force_pad_inf and self.out.shape[1] != lse.shape[2]:
            lse[:, :, self.out.shape[1] :].fill_(math.inf)
        return lse


@dataclass
class Gradients:
    dq: torch.Tensor
    dk: torch.Tensor
    dv: torch.Tensor
    # bias gradient. None if there is no tensor bias or if it doesn't require grad
    db: Optional[torch.Tensor] = None


class AttentionOpBase(BaseOperator):
    """Base class for any attention operator in xFormers

    See:

    - :attr:`xformers.ops.MemoryEfficientAttentionOp`

    - :attr:`xformers.ops.MemoryEfficientAttentionCutlassOp`

    - :attr:`xformers.ops.MemoryEfficientAttentionFlashAttentionOp`

    - :attr:`xformers.ops.MemoryEfficientAttentionCutlassFwdFlashBwOp`
    """

    OPERATOR: Any
    SUPPORTED_DEVICES: Set[str]
    CUDA_MINIMUM_COMPUTE_CAPABILITY: Tuple[int, int] = (5, 0)
    SUPPORTED_DTYPES: Set[torch.dtype]
    SUPPORTED_MAX_K: float
    SUPPORTED_ATTN_BIAS_TYPES: Set[Any] = {type(None)}
    SUPPORTS_DROPOUT: bool
    SUPPORTS_CUSTOM_SCALE: bool = False
    SUPPORTS_DIFFERENT_VALUE_EMBED: bool = False
    NAME: str
    OPERATOR_CATEGORY = "memory_efficient_attention"

    _TEST_BATCH_SIZES: List[int] = [1, 300]
    _TEST_K: List[int] = [32, 128]

    @classmethod
    def supports(cls, d: Inputs) -> bool:
        return not cls.not_supported_reasons(d)

    @classmethod
    def not_supported_reasons(cls, d: Inputs) -> List[str]:
        """
        Returns a list of reasons why this is not supported.
        The kernel can run these inputs only if the returned list is empty
        """
        reasons = []
        device_type = d.query.device.type
        dtype = d.query.dtype
        if device_type not in cls.SUPPORTED_DEVICES:
            reasons.append(f"device={device_type} (supported: {cls.SUPPORTED_DEVICES})")
        if device_type == "cuda" and not _built_with_cuda:
            reasons.append("xFormers wasn't build with CUDA support")
        if dtype not in cls.SUPPORTED_DTYPES:
            reasons.append(f"dtype={dtype} (supported: {cls.SUPPORTED_DTYPES})")
        if (
            not cls.SUPPORTS_DIFFERENT_VALUE_EMBED
            and d.query.shape[-1] != d.value.shape[-1]
        ):
            reasons.append("query.shape[-1] != value.shape[-1]")
        if max(d.query.shape[-1], d.value.shape[-1]) > cls.SUPPORTED_MAX_K:
            reasons.append(
                f"max(query.shape[-1] != value.shape[-1]) > {cls.SUPPORTED_MAX_K}"
            )
        if type(d.attn_bias) not in cls.SUPPORTED_ATTN_BIAS_TYPES:
            reasons.append(f"attn_bias type is {type(d.attn_bias)}")
        if (d.p != 0.0) and not cls.SUPPORTS_DROPOUT:
            reasons.append("dropout > 0.0")
        if d.scale is not None and not cls.SUPPORTS_CUSTOM_SCALE:
            reasons.append("has custom scale")
        # bfloat16 is only supported on A100+
        # ... although the kernels can still run and give the
        # correct result
        if dtype is torch.bfloat16 and (
            not device_type.startswith("cuda")
            or torch.cuda.get_device_capability(d.query.device)[0] < 8
        ):
            reasons.append("bf16 is only supported on A100+ GPUs")
        return reasons


class AttentionFwOpBase(AttentionOpBase):
    ERROR_ATOL: Mapping[torch.dtype, float] = {
        torch.float: 3e-4,
        torch.half: 4e-3,
        torch.bfloat16: 2e-2,
    }
    ERROR_RTOL: Mapping[torch.dtype, float] = {
        torch.float: 2e-5,
        torch.half: 4e-4,
        torch.bfloat16: 5e-3,
    }

    @classmethod
    def apply(
        cls, inp: Inputs, needs_gradient: bool
    ) -> Tuple[torch.Tensor, Optional[Context]]:
        raise NotImplementedError()


class AttentionBwOpBase(AttentionOpBase):
    ERROR_ATOL: Mapping[torch.dtype, float] = {
        torch.float: 5e-4,
        torch.half: 9e-2,
        torch.bfloat16: 0.7,
    }
    ERROR_RTOL: Mapping[torch.dtype, float] = {
        torch.float: 1e-4,
        torch.half: 2e-2,
        torch.bfloat16: 0.1,
    }
    SUPPORTS_ATTN_BIAS_GRAD = False

    @classmethod
    def supports(cls, d: Inputs) -> bool:
        if not super(AttentionBwOpBase, cls).supports(d):
            return False
        if (
            isinstance(d.attn_bias, torch.Tensor)
            and d.attn_bias.requires_grad
            and not cls.SUPPORTS_ATTN_BIAS_GRAD
        ):
            return False

        return True

    @classmethod
    def apply(cls, ctx: Context, inp: Inputs, grad: torch.Tensor) -> Gradients:
        raise NotImplementedError()


AttentionOp = Tuple[
    Optional[Type[AttentionFwOpBase]], Optional[Type[AttentionBwOpBase]]
]


@dataclass
class AttentionOpDispatch:
    """Dispatcher to automatically select
    the best operator to run memory-efficient attention.

    :Deprecated:

        This class is deprecated and will be removed in a later version
    """

    op: AttentionOp

    @classmethod
    def from_arguments(
        cls,
        query: torch.Tensor,
        key: torch.Tensor,
        value: torch.Tensor,
        attn_bias: Optional[Union[torch.Tensor, AttentionBias]] = None,
        p: float = 0.0,
        scale: Optional[float] = None,
    ) -> "AttentionOpDispatch":
        """Here for backward compatibility"""
        from .dispatch import _dispatch_bw, _dispatch_fw

        inp = Inputs(
            query=query,
            key=key,
            value=value,
            attn_bias=attn_bias,
            p=p,
            scale=scale,
        )
        return AttentionOpDispatch(op=(_dispatch_fw(inp), _dispatch_bw(inp)))


def bmk2bmhk(tensor, num_heads: int) -> torch.Tensor:
    if tensor.ndim == 4:
        return tensor
    return tensor.reshape([-1, num_heads, tensor.shape[1], tensor.shape[2]]).permute(
        (0, 2, 1, 3)
    )


def check_lastdim_alignment_stride1(
    reasons: List[str], name: str, x: torch.Tensor, alignment: int
) -> None:
    if x.shape[-1] % alignment != 0:
        reasons.append(f"{name}.shape[-1] % {alignment} != 0")
    elif x.stride(-2) % alignment != 0:
        reasons.append(
            f"{name}.stride(-2) % {alignment} != 0 ({name}.stride() = {x.stride()})"
        )
    # We can have stride=0 sometimes if dimension=1
    if x.stride(-1) > 1:
        reasons.append(
            f"{name}.stride(-1) > 1 ({name}.stride() = {x.stride()}) - you should call `.contiguous()` on the input"
        )
