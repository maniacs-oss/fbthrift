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
import includes.types


# Forward Definitions for Structs
class MyStruct(thrift.py3.types.Struct): ...


class MyStruct(thrift.py3.types.Struct):
    def __init__(
        self, *,
        MyIncludedField: includes.types.Included=None,
        MyOtherIncludedField: includes.types.Included=None,
        MyIncludedInt: int=None
    ) -> None: ...

    def __call__(
        self, *,
        MyIncludedField: _typing.Union[includes.types.Included, NOTSET, None]=NOTSET,
        MyOtherIncludedField: _typing.Union[includes.types.Included, NOTSET, None]=NOTSET,
        MyIncludedInt: _typing.Union[int, NOTSET, None]=NOTSET
    ): ...

    def __reduce__(self) -> _typing.Tuple[Callable, _typing.Tuple[_typing.Type[MyStruct], bytes]]: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Any]]: ...
    def __bool__(self) -> bool: ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: MyStruct) -> bool: ...
    def __lt__(self, other: MyStruct) -> bool: ...

    @property
    def MyIncludedField(self) -> includes.types.Included: ...
    @property
    def MyOtherIncludedField(self) -> includes.types.Included: ...
    @property
    def MyIncludedInt(self) -> int: ...


