#!/usr/bin/env python3
""" Function that return a list """
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Asynchronously generates a list of random numbers."""
    return [result async for result in async_generator()]
