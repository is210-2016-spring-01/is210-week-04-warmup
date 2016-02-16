#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function named too_many_kittens"""


def too_many_kittens(kittens, litterboxes, catfood):

    """This function finds if we have enough litterboxes and catfood for
    each kitten.
    Arguments:
    kittens(int): # of kittens
    litterboxes(int): # of litterboxes available
    catfood(boolean): does catfood exist or not
    Return:
    do we have too many kittens? (true or false)
    Example:
    >>> too_many_kittens(12, 12, False)
    True
    >>> too_many_kittens(12, 12, True)
    False
    """

    return not (litterboxes >= kittens and catfood)
