#!/usr/bin/env python3
"""Function measure_time to measure the total execution time for wait_n"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Returns the total execution time for wait_n"""
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - s
    return elapsed
