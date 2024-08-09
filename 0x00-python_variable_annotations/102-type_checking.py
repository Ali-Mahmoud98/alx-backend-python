#!/usr/bin/env python3
"""
102-type_checking
"""


from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    zoom_array: Returns a list of zoomed in values.

    Args:
        lst (Tuple): The tuple to 'zoom'.
        factor (int, optional): The zoom factor. Defaults to 2.

    Returns:
        List: The zoomed in list.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x: List = zoom_array(array)

zoom_3x: List = zoom_array(array, 3)
