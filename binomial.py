#!/usr/bin/env python
# -*- coding: utf-8 -*-


from math import factorial


def binomial(x, y, verbose=False):
    """Return  the binomial coefficient for x chooses y.
    """

    try:
        result = factorial(x) // factorial(y) // factorial(x - y)
    except ValueError:
        result = 0
    if verbose is True:
        print('b({}, {}) = {}'.format(x, y, result))
    return result
