#!/usr/bin/env python3
"""Type-annotated function sum-list with complex types"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of the floats in input_list"""
    return sum(input_list)
