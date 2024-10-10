#!/usr/bin/env python3
"""Write a type-annotated function safely_get_value that takes
a dictionary, a key, and an optional default value.
It returns the value associated with the key if present,
otherwise it returns the default value.
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any,
                     default: Union[T, None] = None) -> Union[T, None]:
    """Returns the value associated with 'key' in the 'dct' if present,
    otherwise returns 'default'.

    Args:
        dct (Mapping[Any, T]): The dictionary to search.
        key (Any): The key to look for in the dictionary.
        default (Union[T, None], optional): The value to return if
        'key' is not found. Defaults to None.

    Returns:
        Union[T, None]: The value associated with 'key' if it exist
    """
    if key in dct:
        return dct[key]
    else:
        return default
