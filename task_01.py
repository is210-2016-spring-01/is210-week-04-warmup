#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """Defines function to return a string including args described below.

    Args:
        winks (str): String to be included in returned string
        numwink (int): Integer designating the number of repetitions with a
        default of 2.

    Returns:
        restr (str): String containing 'Know what I mean', plus wink
        string repeated as designated by numwink integer.

    Examples:
        >>>know_what_i_mean(wink, 2)
        'Know what I mean? wink wink, nudge nudge'
        >>>know_what_i_mean(spam, 2)
        'Know what I mean? spam spam, nudge nudge'
    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {0}, {1}'.format(winks, nudges)
    return retstr
