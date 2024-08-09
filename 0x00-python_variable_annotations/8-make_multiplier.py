#!/usr/bin/env python3
""" This module contains the make_multiplier function. """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Multiplies a value by a given multiplier.

    Args:
        multiplier (float): The multiplier to multiply the value by.

    Returns:
        Callable[[float], float]: A function that multiplies the value by the
        given multiplier.
    """
    def multiplier_function(value: float) -> float:
        """ Multiplies a value by a given multiplier.

        Args:
            value (float): The value to multiply.

        Returns:
            float: The multiplied value.
        """
        return value * multiplier
    return multiplier_function
