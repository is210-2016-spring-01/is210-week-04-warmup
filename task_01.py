#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """This function does some math and returns a string.

    This is **restructured text** after all.

    Args:
        winks (mixed): Argument to be multiplied with numwink.
        numwink (int, optional): Argument to multiply with nudge. Default: 2

    Returns:
        str: All argumets concatenated with commas.

    Examples:

        know_what_I_mean('winkwink', 'nudgenudge')
    """
    winks = (wink * numwink)
    nudges = ('nudge' * numwink)
    retstr = 'know_what_i_mean'.format(winks, nudges)
    return retstr
