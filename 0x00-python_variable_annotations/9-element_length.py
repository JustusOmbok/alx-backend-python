#!/usr/bin/env python3
"""TASK 9 module
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples.
    Each tuple contains an element from the input list and its length.

    :param lst: The input iterable of sequences.
    :return: A list of tuples
    """
    return [(i, len(i)) for i in lst]
