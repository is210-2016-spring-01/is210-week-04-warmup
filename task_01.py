#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """Does some math and returns a string.

    Args:
        wink (mixed): Arg to be arithmetically multiplied with numwink
        numwink (int): Defined number. Default: 2

    Returns:
        int: All arguements mutiplied with commas

    Examples:

        >>>
    """

    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
