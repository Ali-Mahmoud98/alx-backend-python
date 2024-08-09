#!/usr/bin/env python3
""" This module contains the element_length function. """

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns the length of each element in a list. """
    return [(i, len(i)) for i in lst]
