#!/usr/bin/env python3
"""Type-annotated function sum-list with complex types"""


def sum_list(input_list: list[float]) -> float:
    """Returns the sum of the floats in input_list"""
    sum = 0
    for num in input_list:
        sum += num
    return sum
