#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Checks number of litterboxes and food per cat."""


def too_many_kittens(kittens, litterboxes, catfood):
    """Determines if there is enough food and litterboxes for kittens on hand.

    Args:
        kittens (int): Number of kittens.
        litterboxes (int): Number of litterboxes.
        catfood (bool): Represents whether food exists.

    Returns:
        bool: Returns True if too many kittens.

    Examples:
        >>> too_many_kittens(2, 3, True)
        False

        >>> too_many_kittens(6, 12, False)
        True
    """
    enough = not (litterboxes >= kittens and catfood)
    return enough
