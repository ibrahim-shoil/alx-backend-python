#!/usr/bin/env python3
"""
This module contains an asynchronous function to
run multiple coroutines concurrently
and return the delays in ascending order.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Runs wait_random n times with the specified max_del
    Args:
    n (int): The number of times to call wait_random.
    max_delay (int): The maximum delay for each call to wait_random.

    Returns:
    List[float]: A list of the delays in ascending order.
    """

    # Create a list of tasks to run concurrently using asyncio.gather
    tasks = [await wait_random(max_delay) for _ in range(n)]
    return sorted(tasks)
