#!/usr/bin/env python3
"""Coroutine measure_runtime that executes async_comprehension four times
in parallel"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the total runtime when async_comprehension is executed four
    times in parallel and returns it"""
    s = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    runtime = time.perf_counter() - s
    return runtime
