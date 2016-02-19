#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """This function does some math and returns a string.

    This is **restructured text** after all.

    Args:
        winks (mixed): Argument to be multiplied with numwink.
        numwink (int, optional): Argument to  multiply with nudge. Default: 2
        nudges (str): Argument to be multiplied with numwink.

    Returns:
        str: All argumets concatenated with commas.

    Examples:
    
        know_what_I_mean('winkwink', 'nudgenudge')
    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
