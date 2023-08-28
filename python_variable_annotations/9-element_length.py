#!/usr/bin/env python3
"""Type-annotated function element_length"""

from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples with each element of lst and their len"""
    return [(i, len(i)) for i in lst]
