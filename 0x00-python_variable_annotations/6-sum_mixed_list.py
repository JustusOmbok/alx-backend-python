#!/usr/bin/env python3
"""TASK 6 module
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list of integers and floats and returns their sum.

    :param mxd_lst: The list of integers and floats.
    :return: The sum of the integers and floats in the input list.
    """
    return sum(mxd_lst)
