#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """Declares two parameters, prints a dynamic phrase.

    Keyword Arguments:
       wink (string) -- first parameter any string will work.
       numwink (int) -- second parameter (number of wink and nudge repeats
       defaults at 2).

    Returns:
       retstr -- A string that starts with 'Know what I mean?' and
       includes a predesingnated amount of winks, and nudges.

    Example:
       >>> know_what_i_mean("wink ", 2)
       'Know what I mean? wink wink, nudge nudge'
       >>> know_what_i_mean("Elbow  ", 2)
       'Know what I mean? Elbow  Elbow, nudge nudge'
    """

    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
