#!/usr/bin/env python3
"""
File: 1-concurrent_coroutines.py
"""
import asyncio
import random
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random

# slow version
# async def wait_n(n: int, max_delay: int = 10) -> List[float]:
#     """Return the list of all delays"""
#     return sorted([await wait_random(max_delay) for _ in range(n)])

async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Return the list of all delays in ascending order"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return sorted(await asyncio.gather(*tasks))

# async def wait_n(n: int, max_delay: int) -> List[float]:
#     """doc func"""
#     listDelays = []
#     for _ in range(n):
#         listDelays.append(asyncio.create_task(wait_random(max_delay)))
#     return sorted(await asyncio.gather(*listDelays))
