#!/usr/bin/env python3
'''Module for Task 3.
'''
import asyncio
from typing import Callable

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Creates an asyncio.Task for wait_random(max_delay).

    max_delay: Maximum delay in seconds.
    return: asyncio.Task for wait_random(max_delay).
    '''
    return asyncio.create_task(wait_random(max_delay))
