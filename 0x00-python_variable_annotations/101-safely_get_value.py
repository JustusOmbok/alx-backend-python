#!/usr/bin/env python3
"""Task 11 module
"""
from typing import TypeVar, Mapping, Any, Union, Optional


T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any, default: Optional[T] = None
) -> Union[Any, T]:
    """
    Safely gets a value from a dictionary.

    dct: input dictionary.
    key: key to look for in the dictionary.
    default: default value to return
    if the key is not found (default is None).
    return: value associated with the key if found,
    otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
