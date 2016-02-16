#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """Returns string with exponentiated text by default of 2.

    Args:
        wink (str): String passed to function to be multiplied by numwink.
        numwink (int, default=2): Multiplier for wink string to stripped return.

    Returns:
        retstr (str): String with exponentiated wink in formatted output.

    Examples:
        >>> know_what_i_mean('test')
        'Know what I mean? testest, nudge nudge'

        >>> know_what_i_mean('yes')
        'Know what I mean? yesyes, nudge nudge'
    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {0}, {1}'.format(winks, nudges)
    return retstr
