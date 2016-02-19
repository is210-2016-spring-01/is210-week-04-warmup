#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """Flirts with the person running the code.

    There would be a paragraph here, explaining what's happening
    but it's optional, so for now I'll only aim for three lines
    to take up a nice piece of space.

    Args:
        wink (str): Arg that winks the number of times specified in numwink
        numwink (int): Arg specifies how many times wink is printed. Default = 2

    Returns:
        str: Arguments put together with number of winks and nudges specified
        by the user.

        Examples:

        >>> know_what_i_mean(3, 5)
        'Know what I mean? wink wink wink wink wink, nudge
         nudge nudge nudge nudge'

        >>> know_what_i_mean(3)
        'Know what I mean? wink wink, nudge nudge'
    """

    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
