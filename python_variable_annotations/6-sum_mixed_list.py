#!/usr/bin/env python3
"""
a type-annotated function sum_mixed_list
that takes a list of mixed numbers and returns their sum
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Calculate the sum of all elements in a given list."""
    sum = 0
    for numb in mxd_lst:
        sum += numb
    return sum
