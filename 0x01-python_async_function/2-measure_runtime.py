#!/usr/bin/env python3
'''Module for Task 2.
'''
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Measures the total execution time for wait_n(n, max_delay).

    n: Number of times to spawn wait_random.
    max_delay: Maximum delay in seconds.
    return: Average execution time per operation.
    '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
