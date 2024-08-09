#!/usr/bin/env python3
""" This module contains the to_kv function. """

from typing import Union, Tuple


def to_kv(key: str, value: Union[int, float]) -> Tuple[str, float]:
    """
    Square a value and return a tuple with the key and the squared value.

    Args:
        key (str): The key.
        value (Union[int, float]): The value to square.

    Returns:
        Tuple[str, float]: A tuple with the key and the squared value.
    """
    return key, float(value ** 2)
