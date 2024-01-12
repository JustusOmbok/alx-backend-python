#!/usr/bin/env python3
"""Task 8 module
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier, 
    returns a function that multiplies a float by the multiplier.

    multiplier: The float multiplier.
    return: function that multiplies a float by the given multiplier.
    """
    def multiplier_function(x: float) -> float:
        """
        Multiplies a float by the multiplier.

        x: The input float.
        return: The result of the multiplication.
        """
        return x * multiplier

    return multiplier_function
