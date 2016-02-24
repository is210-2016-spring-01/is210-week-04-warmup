#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """Does some math and returns a string.

    Args:
        wink (str): Arg to be arithmetically incremented with numwink.
        numwink (int): Arg to increment wink.

    Returns:
        str: All arguments concatenated with commas.

    Examples:

        >>> know_what_i_mean('John', 2)
        'Know what I mean? JohnJohn, nudge nudge'

        >>> know_what_i_mean('James', 4)
        'Know what I mean? JamesJamesJamesJames, nudge nudge nudge nudge'
    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean?, {0}, {1}'.format(winks, nudges)
    return retstr
