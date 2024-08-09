#!/usr/bin/env python3
""" Sum mixed list function. """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sums a list of numbers.

    Args:
        mxd_lst (List[Union[int, float]]): The list of numbers to sum.

    Returns:
        float: The sum of the list of numbers.
    """
    return float(sum(mxd_lst))
