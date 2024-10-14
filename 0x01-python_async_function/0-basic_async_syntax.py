#!/usr/bin/env python3
import asyncio  # For asynchronous functionality
import random   # For generating random numbers


async def wait_random(max_delay: int = 10) -> float:
    """
    This asynchronous function waits for a random delay
    between 0 and max_delay seconds.
    Arguments:
    max_delay: The maximum value for the delay in seconds. Default is 10.
    Returns:
    The actual delay (float) it waited before returning.
    """
    # Generate a random float between 0 and max_delay
    delay = random.uniform(0, max_delay)
    # Use asyncio.sleep to wait for the random delay (non-blocking)
    await asyncio.sleep(delay)
    return delay
