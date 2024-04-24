#!/usr/bin/env python3
"""
a type-annotated function sum_list
that takes a list of numbers and returns their sum
"""
from typing import List
def sum_list(input_list: List[float]) -> float:
    """Calculate the sum of all elements in a given list."""
    sum = 0
    for numb in input_list:
        sum += numb
    return sum
