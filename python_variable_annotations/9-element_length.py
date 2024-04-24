#!/usr/bin/env python3
"""
Return the length of the longest sequence in a list of sequences
"""
from typing import Sequence, Tuple, Iterable, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return the length of the longest sequence in a list of sequences."""
    return [(i, len(i)) for i in lst]
