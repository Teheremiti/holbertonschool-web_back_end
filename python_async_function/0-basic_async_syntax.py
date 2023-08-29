#!/usr/bin/env python3
"""Asynchronous coroutine that waits for a random delay"""

import asyncio
import random
import time


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it"""
    s = time.perf_counter()
    await asyncio.sleep(random.uniform(0, max_delay))
    delay = time.perf_counter() - s
    return delay
    