#!/usr/bin/env python3
"""Write a type-annotated function to_kv that takes
string k and an int OR float v as arguments and returns a tuple.
The first element of the tuple is the string k.
The second element is the square of the
int/float v and should be annotated as a float.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """comment
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
