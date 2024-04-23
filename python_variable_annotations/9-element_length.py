#!/usr/bin/python3
"""Annotate the below functions parameters and return
values with the appropriate types
"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
