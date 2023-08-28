#!/usr/bin/env python3
"""Type-annotated function sum-list with complex types"""

vector = list[float]


def sum_list(input_list: vector) -> float:
    """Returns the sum of the floats in input_list"""
    sum = 0
    for num in input_list:
        sum += num
    return sum
