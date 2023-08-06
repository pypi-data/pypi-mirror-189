#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2023 Benedict Harcourt <ben.harcourt@harcourtprogramming.co.uk>
#
# SPDX-License-Identifier: BSD-2-Clause

from __future__ import annotations

from typing import (
    Any,
    Dict,
    List,
    Protocol,
    Sequence,
    Set,
    Type,
    Union,
    TypedDict,
    runtime_checkable,
)

import asyncio
import enum
import dataclasses


@dataclasses.dataclass
class InputEvent:
    pass


@dataclasses.dataclass
class OutputEvent:
    pass


InputQueue = asyncio.Queue[InputEvent]
OutputQueue = asyncio.Queue[OutputEvent]


@runtime_checkable
class IOConfigInterface(Protocol):
    def get_inputs(self) -> Sequence[InputInterface]:
        pass

    def get_outputs(self) -> Sequence[OutputInterface]:
        pass


@runtime_checkable
class InputInterface(Protocol):
    @staticmethod
    def produces_inputs() -> Set[Type[InputEvent]]:
        """
        Defines the set of input events this Input class can produce.
        """

    def bind(self, queue: InputQueue) -> None:
        pass

    async def run(self) -> None:
        pass


@runtime_checkable
class OutputInterface(Protocol):
    @staticmethod
    def consumes_outputs() -> Set[Type[OutputEvent]]:
        """
        Defines the set of output events that this Output class can consume
        :return:
        """

    async def output(self, event: OutputEvent) -> bool:
        """
        Does the work of transmitting the event to the world.
        :param event:
        :return:
        """


@runtime_checkable
class TriggerInterface(Protocol):
    @staticmethod
    def consumes_inputs() -> Set[Type[InputEvent]]:
        pass

    def matches(self, event: InputEvent) -> bool:
        pass


@runtime_checkable
class ConditionInterface(Protocol):
    @staticmethod
    def consumes_inputs() -> Set[Type[InputEvent]]:
        pass

    def allows(self, event: InputEvent) -> bool:
        pass


@runtime_checkable
class ActionInterface(Protocol):
    @staticmethod
    def consumes_inputs() -> Set[Type[InputEvent]]:
        pass

    @staticmethod
    def produces_outputs() -> Set[Type[OutputEvent]]:
        pass

    def bind(self, queue: OutputQueue) -> None:
        pass

    async def act(self, event: InputEvent, state: Dict[str, Any]) -> None:
        pass


@runtime_checkable
class BehaviourInterface(Protocol):
    def add(
        self, component: Union[TriggerInterface, ConditionInterface, ActionInterface]
    ) -> None:
        pass

    def consumes_inputs(self) -> Set[Type[InputEvent]]:
        pass

    def bind_output(self, output: OutputQueue) -> None:
        pass

    async def process(self, event: InputEvent) -> None:
        pass


Component = Union[
    BehaviourInterface,
    IOConfigInterface,
    TriggerInterface,
    ConditionInterface,
    ActionInterface,
]


# pylint: disable=C0103
class ComponentKind(str, enum.Enum):
    Behaviour = "Behaviour"
    Trigger = "Trigger"
    Condition = "Condition"
    Action = "Action"
    IOConfig = "IOConfig"
    Template = "Template"
    DataSource = "DataSource"

    @classmethod
    def values(cls) -> List[str]:
        return list(e for e in cls)

    @classmethod
    def interface(cls, value: ComponentKind) -> Type[Component]:
        _map: Dict[ComponentKind, Type[Component]] = {
            cls.Behaviour: BehaviourInterface,
            cls.Trigger: TriggerInterface,
            cls.Condition: ConditionInterface,
            cls.Action: ActionInterface,
            cls.IOConfig: IOConfigInterface,
        }

        if value in _map:
            return _map[value]

        raise ValueError(f"Invalid value {value}")


class ConfigBlock(TypedDict):
    """Common YAML Block for all components"""

    kind: str
    implementation: str
    uuid: str
    properties: Dict[str, Any]


class BehaviourConfigBlock(ConfigBlock):
    """YAML block for a behaviour, which includes the subcomponents"""

    triggers: List[ConfigBlock]
    conditions: List[ConfigBlock]
    actions: List[ConfigBlock]


__all__ = [
    "ComponentKind",
    "Component",
    "IOConfigInterface",
    "InputInterface",
    "OutputInterface",
    "BehaviourInterface",
    "TriggerInterface",
    "ConditionInterface",
    "ActionInterface",
    "InputEvent",
    "OutputEvent",
    "InputQueue",
    "OutputQueue",
    "ConfigBlock",
    "BehaviourConfigBlock",
]
