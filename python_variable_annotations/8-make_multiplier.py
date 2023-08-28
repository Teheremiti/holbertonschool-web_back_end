#!/usr/bin/env python3
"""Type-annotated function make_multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier"""

    def mul(n: float) -> float:
        """Inner function that returns the product of n and multipler"""
        return n * multiplier

    return mul
