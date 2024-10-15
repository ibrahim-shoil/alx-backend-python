#!/usr/bin/env python3
"""
0-async_generator.py
This module contains an asynchronous generator that
yields random numbers between 0 and 10.
The generator pauses for 1 second before yielding
each number and loops exactly 10 times.
Functions:
async_generator:
    An asynchronous generator that yields 10
    random float values between 0 and 10,
    with a 1-second asynchronous pause between each value.
Usage:
-----------
You can use this asynchronous generator in other coroutines
by looping over it with 'async for',
allowing you to retrieve the yielded values asynchronously.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator that yields random
    float numbers between 0 and 10.
    The generator waits asynchronously for
    1 second before yielding each number.
    It yields 10 values in total.
    Yields:
    --------
    float:
        A random float number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
