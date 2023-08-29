#!/usr/bin/env python3
"""Async routine task_wait_n"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns task_wait_random n times with the specified max_delay"""
    delays = []
    for _ in range(n):
        delays.append(task_wait_random(max_delay))
    results = await asyncio.gather(*delays)
    return sorted(results)
