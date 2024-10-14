#!/usr/bin/env python3
"""
This module demonstrates asynchronous programmin
using the `asyncio` module
It contains a coroutine that waits for a random
amount of time and returns that delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous function that waits for a random
    delay between 0 and max_delay seconds.

    Args:
    max_delay (int): The maximum delay in seconds. Default is 10.

    Returns:
    float: The actual delay waited in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
