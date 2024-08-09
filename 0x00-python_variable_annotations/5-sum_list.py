#!/usr/bin/env python3
""" Sum list function. """

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sums a list of numbers.

    Args:
        input_list (List[float]): The list of numbers to sum.

    Returns:
        float: The sum of the list of numbers.
    """
    return sum(input_list)
