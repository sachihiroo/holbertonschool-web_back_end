#!/usr/bin/env python3
"""
a type-annotated function make_multiplier
returns a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiplies a float by multiplier"""
    def multiplyer(x: float) -> float:
        return x * multiplier
    return multiplyer
