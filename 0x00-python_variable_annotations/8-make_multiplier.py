#!/usr/bin/env python3
"""Task 8 module
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier, returns a function that multiplies a float by the multiplier.

    multiplier: The float multiplier.
    return: A function that multiplies a float by the given multiplier.
    """
    return lambda x: x * multiplier
