#!/usr/bin/env python
# -*- coding: utf-8 -*-


def starsnbars(stars, bars, minimum=0):
    """Return a generator of all k-tuples for a given sum and size.

    See https://en.wikipedia.org/wiki/Stars_and_bars_(combinatorics).

    stars   -- value that each tuple must sum to
    bars    -- number of members in each tuple
    minimum -- minimum value for each member of each tuple
    """

    if bars == 0:
        yield (stars,)
    else:
        for i in range(minimum, stars - minimum * bars + 1):
            for it in starsnbars(stars - i, bars - 1, minimum):
                yield (stars - (stars - i),) + it
