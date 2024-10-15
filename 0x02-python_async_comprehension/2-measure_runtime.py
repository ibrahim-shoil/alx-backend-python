#!/usr/bin/env python3
"""
2-measure_runtime.py

This module contains a function to
measure the time it takes to execute
an asynchronous comprehension four times in parallel.

Functions:
-----------
measure_runtime:
    Measures the total runtime for running
    async_comprehension four times concurrently.
"""

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime for executing `async_comprehension`
    four times in parallel.
    This function uses `asyncio.gather` to run four instances of
    `async_comprehension`
    concurrently. It measures the time taken to execute all
    four in parallel and
    returns the total time.
    Returns:
    --------
    float:
        The time, in seconds, that it took to execute `async_comprehension`
        four times concurrently.
    """
    start = time.perf_counter()  # Start time measurement
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    return time.perf_counter() - start  # Calculate and return the elapsed time