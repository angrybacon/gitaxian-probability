#!/usr/bin/env python
# -*- coding: utf-8 -*-


def cache(feature):
    """Hack'ish and pretty straightforward cache for heavier calculations.

    Usage:
      f = cache(f)
      f(x, y)
      f(z)

    feature -- the function to cache results for
    """

    cache = {}
    def decorator(*args):
        if args in cache:
            return cache[args]
        else:
            result = feature(*args)
            cache[args] = result
            return result
    return decorator
