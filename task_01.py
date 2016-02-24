#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """Returns a string including a specified number of winks and nudges.

    Args:
        wink (string): The phrase to be used as the 'wink'.

        numwink (integer): The number of times the wink phrase is to be
                        repeated.

    Returns:
        string: starts with 'Know what I mean? ' plus the winks and nudges`

    Examples:
        >>> know_what_i_mean('wink ')
        Know what I mean? wink wink, nudge nudge

        >>> know_what_i_mean('is she a goer ', 3)
        Know what I mean? is she a goer is she a goer is she a goer,
        nudge nudge nudge
    """

    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {0}, {1}'.format(winks, nudges)
    return retstr
