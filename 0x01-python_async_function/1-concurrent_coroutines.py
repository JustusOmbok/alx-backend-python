#!/usr/bin/env python3
"""Module for tsk 1
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times
    with the specified max_delay.

    n: Number of times to spawn wait_random.
    max_delay: Maximum delay in seconds.
    return: List of delays in ascending order.
    """
    delays = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(delays)
