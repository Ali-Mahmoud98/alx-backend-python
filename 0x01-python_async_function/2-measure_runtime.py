#!/usr/bin/env python3
"""
File: 2-measure_runtime.py
"""

import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


# def measure_time(n: int, max_delay: int) -> float:
#     """measure the total runtime for wait_n"""
#     start = time.perf_counter()
#     asyncio.run(wait_n(n, max_delay))
#     end = time.perf_counter()
#     return (end - start) / n

def measure_time(n: int, max_delay: int) -> float:
    """measure the total runtime for wait_n"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
