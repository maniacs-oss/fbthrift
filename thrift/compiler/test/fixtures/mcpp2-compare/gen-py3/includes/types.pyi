#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

import thrift.py3.types
import thrift.py3.exceptions
from thrift.py3.types import NOTSET
from thrift.py3.serializer import Protocol
import typing as _typing

import sys
import itertools
from enum import Enum


class AnEnum(Enum):
    FIELDA: ...
    FIELDB: ...
    value: int


# Forward Definitions for Structs
class AStruct(thrift.py3.types.Struct): ...
class AStructB(thrift.py3.types.Struct): ...


class AStruct(thrift.py3.types.Struct):
    def __init__(
        self, *,
        FieldA: int=None
    ) -> None: ...

    def __call__(
        self, *,
        FieldA: _typing.Union[int, NOTSET, None]=NOTSET
    ): ...

    def __reduce__(self) -> _typing.Tuple[Callable, _typing.Tuple[_typing.Type[AStruct], bytes]]: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Any]]: ...
    def __bool__(self) -> bool: ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: AStruct) -> bool: ...
    def __lt__(self, other: AStruct) -> bool: ...

    @property
    def FieldA(self) -> int: ...


class AStructB(thrift.py3.types.Struct):
    def __init__(
        self, *,
        FieldA: AStruct=None
    ) -> None: ...

    def __call__(
        self, *,
        FieldA: _typing.Union[AStruct, NOTSET, None]=NOTSET
    ): ...

    def __reduce__(self) -> _typing.Tuple[Callable, _typing.Tuple[_typing.Type[AStructB], bytes]]: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Any]]: ...
    def __bool__(self) -> bool: ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: AStructB) -> bool: ...
    def __lt__(self, other: AStructB) -> bool: ...

    @property
    def FieldA(self) -> AStruct: ...


