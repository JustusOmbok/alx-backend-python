#!/usr/bin/env python3
'''Module for Task 4.
'''
import asyncio
from typing import List, Callable

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes task_wait_random n times.

    n: Number of times to spawn task_wait_random.
    max_delay: Maximum delay in seconds.
    return: List of delays in ascending order.
    '''
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)
