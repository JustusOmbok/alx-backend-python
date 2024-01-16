#!/usr/bin/env python3
'''Module for Task 2.
'''
import asyncio
from time import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Measures the total runtime of executing async_comprehension four times
    in parallel.
    '''
    start_time = time()

    # Run async_comprehension four times in parallel using asyncio.gather
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())

    end_time = time()

    # Return the total runtime
    return end_time - start_time
