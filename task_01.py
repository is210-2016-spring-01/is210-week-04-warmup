#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """This function does some math and returns a string.

    Args:
        wink (str): Argument to be incremented by numwink.
        numwink (int): Argument to increment wink.

    Returns:
        Arguments concatenated after an original string 'Know what I mean'.

    Examples:

        >>>know_what_i_mean(winks, nudges)
        Know what I mean? winkwink, nudgenudge.
    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {0}, {1}'.format(winks, nudges)
    return retstr
