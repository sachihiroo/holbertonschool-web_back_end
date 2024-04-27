#!/usr/bin/env python3
"""
execute multiple coroutines at the same time with async
"""
from typing import List
import asyncio


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Wait for n seconds and return a random number between 1 to max_delay.
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delay_list = await asyncio.gather(*coroutines)
    return sorted(delay_list)
