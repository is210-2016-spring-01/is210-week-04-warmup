#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """Multiples str by int and adds it to string.

    Args:
        wink (str): String to be multiplied.
        numwink (int, optional): Multiplying integer.

    Returns:
        str: Formatted string with winks and nudges.

    Examples:

        >>> know_what_i_mean('me')
        'Know what I mean? meme, nudge nudge'>>> myfunc(2,3)

        >>> know_what_i_mean('wink ',3)
        'Know what I mean? wink wink wink, nudge nudge nudge'
    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {0}, {1}'.format(winks, nudges)
    return retstr
