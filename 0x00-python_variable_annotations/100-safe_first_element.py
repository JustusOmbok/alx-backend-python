#!/usr/bin/env python3
"""Task 10 module
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the input list, or None if the list is empty.

    lst: input list of elements.
    return: first element of the list or None if the list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
