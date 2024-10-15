#!/usr/bin/env python3
"""1-async_comprehension.py"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async
    comprehension over async_generator.
    """
    result = [i async for i in async_generator()]
    return result