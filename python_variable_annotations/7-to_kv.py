#!/usr/bin/env python3
"""Type-annotated function to_kv"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple that consists of k and v squared"""
    return (k, v**2)
