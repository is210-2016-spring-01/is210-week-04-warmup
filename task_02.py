#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module does some pretty crazy math."""


import hamlet


def crazy_math(myvar):
    """ Testing the crazy math equation.

    Args:
        myvar (var): Imports the crazy_math function from hamlet

    Returns:
        decimal: end result to equation

    Example:
        >>> hamlet.crazy_math(4, 100000, 8, 98)
        '0.00374391674995'
    """

    myvar = hamlet.crazy_math(4, 100000, 8, 98)
    return myvar

POSITIONAL = hamlet.crazy_math(4, 100000, 8, 98)
