#!/usr/bin/env python3
"""Task 12 module"""
from typing import List, Tuple


def zoom_array(lst: List, factor: int = 2) -> Tuple:
    zoomed_in: Tuple = tuple([
        item for item in lst
        for i in range(factor)
    ])
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
