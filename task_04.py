#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module calculates there is enough catfood and litterboxes."""


def too_many_kittens(kittens, litterboxes, catfood):
    """A function to see if there's at least one litterbox per kitten and food.

    Args:
        kittens (int): Number of kittens.
        litterboxes (int): Number of available litterboxes.
        catfood (bool): Does catfood exist?

    Returns:
        bool: Whether or not catfood exists after calculation.

    Examples:

        >>> too_many_kittens(13, 12, True)
        True

        >>> too_many_kittens(5, 6, False)
        True
    """
    return not (litterboxes >= kittens and catfood)
