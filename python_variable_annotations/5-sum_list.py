#!/usr/bin/env python3
"""
a type-annotated function sum_list
that takes a list of numbers and returns their sum
"""


def sum_list(input_list: list[float]) -> float:
    """Calculate the sum of all elements in a given list."""
    return sum(input_list)
