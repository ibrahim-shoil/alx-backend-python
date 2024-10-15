#!/usr/bin/env python3


import asyncio
import random


async def async_generator():
    """
    Asynchronous generator that yields random float numbers between 0 and 10.
    The generator waits asynchronously for 1 second before yielding each.
    It yields 10 values in total.
    Yields:
    --------
    float: A random float number between 0 and 10.
    """

    for _ in range(10):  # Loop 10 times
        await asyncio.sleep(1)  # Wait for 1 second asynchronously
        yield random.uniform(0, 10)  # Yield a random float between 0 and 10
