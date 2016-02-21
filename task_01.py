#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """ This function knows what you mean

    Args:
        wink (str): arg to be multipled with numwink
        numwink (int): arg to implement winks and nudges. Default: 2

    Returns:
        str: All arguments to be concatenated with commas

    Examples:
        >>> know_what_i_mean(3, numwink)
        '3, 2'

    """

    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
