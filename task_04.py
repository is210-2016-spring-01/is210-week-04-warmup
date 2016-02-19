#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module determines if there are too many kittens for the available
   cat food and litterboxes.
"""


def too_many_kittens(kittens, litterboxes, catfood):
    """Defines a function to calculate whethere there are too many kittens
    for the amount of catfood and litterboxes present.

    Args:
        kittens (int): Number of kittens
        litterboxes (int): Number of litterboxes
        catfood (bool): Whether or not there is cat food

    Returns:
        bool: Whether there are too many kittens for the amount
        of litterboxes and catfood present.

    Examples:
    >>> too_many_kittens(12, 12, False)
    True

    >>> too_many_kittens(13, 12, True)
    True

    >>> too_many_kittens(12, 13, True)
    False

    """

    return not (litterboxes >= kittens and catfood)
