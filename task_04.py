#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module does some booleans."""


def too_many_kittens(kittens, litterboxes, catfood):
    """Calculates the litter boxes for catfood

    Args:
        Kittens (int): Arguments shows the number of kittens.
        litterboxes (int): Argument shows the number of litterboxes.
        catfood (boolean): Arguments shows if there is catfood.

    Returns:
        str: Arguments in a boolean statement.

    Examples:
        >>> too_many_kittens(6, 6, False)
        True
        >>> too_many_kittens(13, 12, True)
        True
        >>> too_many_kittens(5, 5, False)
        True
    """
    return not (litterboxes >= kittens and catfood)
