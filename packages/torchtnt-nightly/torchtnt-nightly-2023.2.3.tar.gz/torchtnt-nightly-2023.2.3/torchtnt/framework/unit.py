# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

# Disable `Any` type errors
# pyre-ignore-all-errors[2]
# pyre-ignore-all-errors[3]

from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, TypeVar

import torch

from torchtnt.framework.state import State
from torchtnt.utils import TLRScheduler
from typing_extensions import Protocol, runtime_checkable

"""
This file defines mixins and interfaces for users to customize hooks in training, evaluation, and prediction loops.
"""


@runtime_checkable
class _Stateful(Protocol):
    def state_dict(self) -> Dict[str, Any]:
        ...

    def load_state_dict(self, state_dict: Dict[str, Any]) -> None:
        ...


def _remove_from_dicts(name_to_remove: str, *dicts: Dict[str, Any]) -> None:
    for d in dicts:
        if name_to_remove in d:
            del d[name_to_remove]


class AppStateMixin:
    """
    A mixin to track modules, optimizers, and LR schedulers to simplify checkpointing object states.
    This can be easily extended to cover types that conform to the Stateful protocol.
    The logic here is adapted from torch.nn.Module's handling to register states for buffers, parameters, and modules.
    """

    def __init__(self) -> None:
        self._modules: Dict[str, torch.nn.Module] = {}
        self._optimizers: Dict[str, torch.optim.Optimizer] = {}
        self._lr_schedulers: Dict[str, TLRScheduler] = {}
        # catch-all for miscellaneous statefuls
        self._misc_statefuls: Dict[str, Any] = {}
        # TODO: include other known statefuls

    def app_state(self) -> Dict[str, Any]:
        """Join together all of the tracked stateful entities to simplify registration of snapshottable states"""
        # TODO: refine with Stateful typehint
        # TODO: Should we split this into app_state_to_load and app_state_to_save
        # in order to let users customize the saving & loading paths independently?
        # or should we assume this is done outside of the loop framework entirely?
        app_state = {
            **self.tracked_modules(),
            **self.tracked_optimizers(),
            **self.tracked_lr_schedulers(),
            **self.tracked_misc_statefuls(),
        }
        return app_state

    def tracked_modules(self) -> Dict[str, torch.nn.Module]:
        return self._modules

    def tracked_optimizers(self) -> Dict[str, torch.optim.Optimizer]:
        return self._optimizers

    def tracked_lr_schedulers(
        self,
    ) -> Dict[str, TLRScheduler]:
        return self._lr_schedulers

    def tracked_misc_statefuls(self) -> Dict[str, Any]:
        return self._misc_statefuls

    def __getattr__(self, name: str) -> Any:
        if "_modules" in self.__dict__:
            _modules = self.__dict__["_modules"]
            if name in _modules:
                return _modules[name]
        if "_optimizers" in self.__dict__:
            _optimizers = self.__dict__["_optimizers"]
            if name in _optimizers:
                return _optimizers[name]
        if "_lr_schedulers" in self.__dict__:
            _lr_schedulers = self.__dict__["_lr_schedulers"]
            if name in _lr_schedulers:
                return _lr_schedulers[name]
        if "_misc_statefuls" in self.__dict__:
            _misc_statefuls = self.__dict__["_misc_statefuls"]
            if name in _misc_statefuls:
                return _misc_statefuls[name]

        return self.__getattribute__(name)

    def _update_attr(
        self,
        name: str,
        value: Any,
        tracked_objects: Dict[str, Any],
    ) -> None:
        if tracked_objects is None:
            raise AttributeError(
                "cannot assign parameter before _AppStateMixin.__init__() call"
            )
        _remove_from_dicts(
            name,
            self.__dict__,
            self._modules,
            self._optimizers,
            self._lr_schedulers,
            self._misc_statefuls,
        )
        tracked_objects[name] = value

    def __setattr__(self, name: str, value: Any) -> None:
        if isinstance(value, torch.nn.Module):
            self._update_attr(name, value, self.__dict__.get("_modules"))
        elif isinstance(value, torch.optim.Optimizer):
            self._update_attr(name, value, self.__dict__.get("_optimizers"))
        elif isinstance(value, TLRScheduler):
            self._update_attr(
                name,
                value,
                self.__dict__.get("_lr_schedulers"),
            )
        elif isinstance(value, _Stateful):
            self._update_attr(
                name,
                value,
                self.__dict__.get("_misc_statefuls"),
            )
        else:
            if value is None:
                _remove_from_dicts(
                    name,
                    self.__dict__,
                    self._modules,
                    self._optimizers,
                    self._lr_schedulers,
                    self._misc_statefuls,
                )
            super().__setattr__(name, value)

    def __delattr__(self, name: str) -> None:
        if name in self._modules:
            del self._modules[name]
        elif name in self._optimizers:
            del self._optimizers[name]
        elif name in self._lr_schedulers:
            del self._lr_schedulers[name]
        elif name in self._misc_statefuls:
            del self._misc_statefuls[name]
        else:
            super().__delattr__(name)


class _OnExceptionMixin:
    def on_exception(self, state: State, exc: BaseException) -> None:
        pass


TTrainData = TypeVar("TTrainData")
TEvalData = TypeVar("TEvalData")
TPredictData = TypeVar("TPredictData")


class TrainUnit(AppStateMixin, _OnExceptionMixin, Generic[TTrainData], ABC):
    """
    Base interface for training.
    """

    def on_train_start(self, state: State) -> None:
        pass

    def on_train_epoch_start(self, state: State) -> None:
        pass

    @abstractmethod
    def train_step(self, state: State, data: TTrainData) -> Any:
        ...

    def on_train_epoch_end(self, state: State) -> None:
        pass

    def on_train_end(self, state: State) -> None:
        pass


class EvalUnit(AppStateMixin, _OnExceptionMixin, Generic[TEvalData], ABC):
    def on_eval_start(self, state: State) -> None:
        pass

    def on_eval_epoch_start(self, state: State) -> None:
        pass

    @abstractmethod
    def eval_step(self, state: State, data: TEvalData) -> Any:
        """
        Optionally can be decorated with ``@torch.inference_mode()`` for improved peformance.
        """
        ...

    def on_eval_epoch_end(self, state: State) -> None:
        pass

    def on_eval_end(self, state: State) -> None:
        pass


class PredictUnit(AppStateMixin, _OnExceptionMixin, Generic[TPredictData], ABC):
    def on_predict_start(self, state: State) -> None:
        pass

    def on_predict_epoch_start(self, state: State) -> None:
        pass

    @abstractmethod
    def predict_step(self, state: State, data: TPredictData) -> Any:
        """
        Optionally can be decorated with ``@torch.inference_mode()`` for improved peformance.
        """
        ...

    def on_predict_epoch_end(self, state: State) -> None:
        pass

    def on_predict_end(self, state: State) -> None:
        pass


TTrainUnit = TrainUnit[TTrainData]
TEvalUnit = EvalUnit[TEvalData]
TPredictUnit = PredictUnit[TPredictData]
