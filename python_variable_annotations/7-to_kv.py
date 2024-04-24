#!/usr/bin/env python3
"""
a type-annotated function to_kv.
returns a tuple.
"""
from typing import List, Tuple


def to_kv(k: str, v: int | float) -> Tuple[str, float]:
    """
    converts key and value into a tuple of strings.
    key is the first element in the tuple,
    value is the second.
    """
    return k, str(v**2)
