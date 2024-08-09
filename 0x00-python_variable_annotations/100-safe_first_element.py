#!/usr/bin/env python3
""" This module contains the safe_first_element function. """

from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Returns the first element of a list.
    If lst is empty, return None.
    Sequence[Any] means that lst is a list of any type.

    Args:
        lst (Sequence[Any]): The list to get the first element from.

    Returns:
        Optional[Any]: The first element of the list.
        Optional[Any] means that the function can return None.
    """
    if lst:
        return lst[0]
    else:
        return None
