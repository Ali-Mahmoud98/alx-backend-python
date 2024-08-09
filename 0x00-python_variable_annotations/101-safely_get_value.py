#!/usr/bin/env python3
""" This module contains the safely_get_value function. """

from typing import Any, Optional, Union, Mapping, TypeVar


T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Safely get a value from a dictionary.

    Args:
        dct (Mapping[Any, Any]): The dictionary to get the value from.
        key (Any): The key to get the value from the dictionary.
        default (Optional[Union[T, None]]): The default value to return
            if the key is not found in the dictionary.

    Returns:
        Union[Any, T]: The value from the dictionary or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
