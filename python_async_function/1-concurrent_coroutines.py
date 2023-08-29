#!/usr/bin/env python3
"""Async routine wait_n"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times with the specified max_delay"""
    delays = []
    for _ in range(n):
        delays.append(wait_random(max_delay))
    results = await asyncio.gather(*delays)
    return sorted(results)
