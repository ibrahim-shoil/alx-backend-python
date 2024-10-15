import asyncio
import random


async def async_generator():
    for _ in range(10):  # Loop 10 times
        await asyncio.sleep(1)  # Wait for 1 second asynchronously
        yield random.uniform(0, 10)  # Yield a random float between 0 and 10
