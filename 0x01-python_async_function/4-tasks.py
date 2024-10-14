#!/usr/bin/env python3
"""
This module contains a function that runs multiple coroutines concurrently
using tasks and returns the delays in ascending order.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run task_wait_random n times with the specified max_delay, concurrently.
    Args:
    n (int): The number of tasks to run.
    max_delay (int): The maximum delay for each task.
    Returns:
    List[float]: A list of the delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
