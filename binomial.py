#!/usr/bin/env python
# -*- coding: utf-8 -*-


from math import factorial


def binomial(x, y):
    """Return  the binomial coefficient for x chooses y.
    """

    try:
        result = factorial(x) // factorial(y) // factorial(x - y)
    except ValueError:
        result = 0
    return result
