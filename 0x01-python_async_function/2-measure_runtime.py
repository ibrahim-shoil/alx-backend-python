#!/usr/bin/env python3
"""
This module contains a function to
measure the runtime of wait_n(n, max_delay)
and return the average time per coroutine.
"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay) and return the
    average time per coroutine.
    Args:
    n (int): The number of times to call wait_random via wait_n.
    max_delay (int): The maximum delay for each call to wait_random.

    Returns:
    float: The average time taken per coroutine.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
