#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Another small docstring"""


def too_many_kittens(kittens, litterboxes=1, catfood=True):
    """A function defining kittens.

    Args:
        kittens (mixed): Can be a number or a string
        litterbox (int): Defined number. Default: 1
        catfood (condition): Boolean statement of the function. Default: True

    Returns:
        condition: All arguments compared with commas

    Examples:

        >>> too_many_kittens(12, 12, False)
        True

        >>> too_many_kittens(13, 12, True)
        True

        >>> too_many_kittens(12,13, True)
        False
    """
    return not (litterboxes >= kittens and catfood)
