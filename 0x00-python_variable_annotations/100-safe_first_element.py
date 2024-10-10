#!/usr/bin/env python3
"""Defines a type-annotated function `element_length`.

The function takes an iterable of sequences and returns a list
of tuples. Each tuple contains a sequence from the input iterable
and its corresponding length as an integer.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Takes an iterable of sequences and returns a list of tuple
    Each tuple contains:
        - A sequence from the input iterable.
        - The length of that sequence as an integer.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where each tuple
        contains a sequence and its length.
    """
    return [(i, len(i)) for i in lst)
