#!/usr/bin/env python3

"""tasks"""

import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """a function that takes an integer and returns a asyncio.Task."""

    return asyncio.Task(wait_random(max_delay))
