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


# Forward Definitions for Containers
class std_unordered_map__Map__i32_string(_typing.Mapping[int, str]): ...


class std_unordered_map__Map__i32_string(_typing.Mapping[int, str]):
    def __init__(self, items: _typing.Mapping[int, str]=None) -> None: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: _typing.Mapping[int, str]) -> bool: ...
    def __getitem__(self, key: int) -> str: ...
    def __iter__(self) -> _typing.Iterator[int]: ...
    def __contains__(self, key: int) -> bool: ...
    def get(self, key: int, default: str=None) -> str: ...
    def keys(self) -> _typing.Iterator[int]: ...
    def values(self) -> _typing.Iterator[str]: ...
    def items(self) -> _typing.Iterator[_typing.Tuple[int, str]]: ...


