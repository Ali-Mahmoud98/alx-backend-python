#!/usr/bin/env python3
"""wait_random coroutine"""


async def wait_random(max_delay: int = 10) -> float:
    """Return the float number of seconds"""
    import random
    import asyncio

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
