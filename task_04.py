#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module will create a new function for practice"""


def too_many_kittens(kittens, litterboxes, catfood):
    """This function does some math and returns a string.

    Args:
        kittens (int): Argument that gives the number of kittens.
        litterboxes (int): Argument that gives the number of available litters.
        catfood (bool): Argument that represents whether or not any catfood \
        exists.

    Returns:
        bool: All arguments must return a boolean value.

    Examples:

        >>> too_many_kitens(12, 12, False)
        True

        >>> too_many_kittens(13, 12, True)
        True

        >>> too_many_kittens(12, 1, True)
        False
    """
    return not (litterboxes >= kittens and catfood)
