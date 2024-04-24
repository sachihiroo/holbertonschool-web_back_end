#!/usr/bin/env python3
"""
a type-annotated function to_kv.
returns a tuple.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    converts key and value into a tuple of strings.
    key is the first element in the tuple,
    value is the second.
    """
    return k, (v**2)
