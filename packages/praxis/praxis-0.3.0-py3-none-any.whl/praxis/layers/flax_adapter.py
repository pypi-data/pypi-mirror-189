# coding=utf-8
# Copyright 2022 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A generic flax.nn.Module adapter layers."""

import abc
import functools
from typing import Any, Callable, Optional

import flax.linen as nn
from flax.linen import partitioning as flax_partitioning
from praxis import base_layer
from praxis import flax_utils
from praxis import pytypes

JTensor = pytypes.JTensor
LogicalAxisRules = pytypes.LogicalAxisRules


class FlaxModuleAdapterBase(base_layer.BaseLayer, metaclass=abc.ABCMeta):
  """Base class for converting an arbitrary nn.Module into a proper Pax Layer.

  Subclasses must implement a `_build_wrapped_module()` method that instantiates
  the nn.Module.

  This adapter assumes that the module has a single compact method __call__. If
  this constraint is not satisfied, a similar adapter can be easily constructed.

  Attributes:
    logical_axes_rules: Optional logical axes rules, e.g., [('input', 'mdl'),
      ('output', 'data')]
  """
  logical_axes_rules: Optional[LogicalAxisRules] = None

  def setup(self) -> None:
    # Construct the child, which can be an arbitrary nn.Module.
    self.cld: nn.Module = self._build_wrapped_module()
    assert isinstance(self.cld, nn.Module)

  @abc.abstractmethod
  def _build_wrapped_module(self) -> nn.Module:
    """Builds the Flax module to be wrapped by this layer."""
    pass

  def _call_with_boxed_params_init(self, unbound_method, *args, **kwargs):

    def call_fn(module, *args, **kwargs):
      # axis_rules context manager is used to map activation sharding logical
      # axes to mesh axes names that pjit expects.
      with flax_partitioning.axis_rules(self.logical_axes_rules):
        return unbound_method(module, *args, **kwargs)

    if not self.is_initializing():
      return call_fn(self.cld, *args, **kwargs)

    # For layer initialization path, need to create BoxedParams.
    # Combine 'params' and 'params_axes' collections into a BoxedParams
    # collection with WeightHParams and tensor_split_dims_mapping derived
    # from Flaxformer's logical axis rules. All other collections are left
    # unchanged.
    mapped_fn = nn.map_variables(
        call_fn,
        mapped_collections=True,  # Transform the entire var col tree.
        mutable=True,
        # The module may be called multiple times during initialization. If this
        # occurs, we must provide it with unboxed versions of the params it
        # previously created.
        trans_in_fn=base_layer.maybe_unbox_value,
        trans_out_fn=functools.partial(
            flax_utils.convert_to_boxed_params,
            logical_axes_rules=self.logical_axes_rules,
            mesh_shape=self.mesh_shape,
        ),
    )

    # Call the final mapped_fn.
    return mapped_fn(self.cld, *args, **kwargs)

  def __call__(self, *args, **kwargs):
    # Note that `__func__` retrieves the unbound method that takes module as
    # the first argument.
    return self._call_with_boxed_params_init(
        self.cld.__call__.__func__, *args, **kwargs  # pytype: disable=attribute-error
    )


class FlaxModuleAdapter(FlaxModuleAdapterBase):
  """Adapts an nn.Module built from a factory function.

  Attributes:
    module_factory_method: A callable that constructs an instance of a module.
  """
  module_factory_method: Optional[Callable[[], Any]] = None

  def _build_wrapped_module(self) -> nn.Module:
    if self.module_factory_method is None:
      raise ValueError('module_factory_method must be set.')
    return self.module_factory_method()


class EncoderDecoderFlaxModuleAdaptor(FlaxModuleAdapter):
  """Similar to FlaxModuleAdapter, but it also have encode/decode methods."""

  def encode(self, *args, **kwargs):
    return self._call_with_boxed_params_init(
        self.cld.encode.__func__, *args, **kwargs  # pytype: disable=attribute-error
    )

  def decode(self, *args, **kwargs):
    return self._call_with_boxed_params_init(
        self.cld.decode.__func__, *args, **kwargs  # pytype: disable=attribute-error
    )

  def compute_logits(self, *args, **kwargs):
    return self._call_with_boxed_params_init(
        self.cld.compute_logits.__func__, *args, **kwargs  # pytype: disable=attribute-error
    )


# TODO(austinwaters): verify that post_init_hparams does something reasonable
# when hparams contain a fdl.Config.
class FiddleFlaxModuleAdapter(FlaxModuleAdapterBase):
  """Adapts an nn.Module built from a fdl.Config.

  Attributes:
    fdl_config: A fdl.Config expressing the module to be created.
  """
  flax_module_factory: Optional[Callable[[], nn.Module]] = None

  def _build_wrapped_module(self) -> nn.Module:
    if self.flax_module_factory is None:
      raise ValueError('flax_module_factory must be set.')
    return self.flax_module_factory()
