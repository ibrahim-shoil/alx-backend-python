#!/usr/bin/env python3
"""Write a type-annotated function element_length that takes
an iterable of sequences and returns a list of tuples.
Each tuple contains a sequence from the input iterable
and its corresponding length as an integer.
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples, where each tuple contains a sequence
    from the input iterable and its length as an integer.
    """
    return [(i, len(i)) for i in lst]
