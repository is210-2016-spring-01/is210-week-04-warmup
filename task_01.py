#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """Playing with some numbers and strings, and return a string

    Args:
        wink (str): Arg to be assigned a value.
        numwink (int): Arg to help duplicate given value by 2 times.

    Returns:
        retstr (str): A string to be returned from the given strings

    Examples:

        >>> know_what_i_mean('2')
        'Know what I mean? 22, nudge nudge'

        >>> know_what_i_mean('headache')
        'Know what I mean? headacheheadache, nudge nudge'
    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {0}, {1}'.format(winks, nudges)
    return retstr
