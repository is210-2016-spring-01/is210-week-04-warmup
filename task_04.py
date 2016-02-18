#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""Task 4, new file."""


def too_many_kittens(kittens, litterboxes, catfood):
    """To calculate if there is too many cats.

    Args:
        kittens (int): number of kittens.
        litterboxes (int): number of litterboxes.
        catfood (bool): to see if any catfood exists.

    Returns:
        bool: to see if we have too many kittens.

    Examples:

        >>> too_many_kittens(13, 12, True)
        'True'

        >>> too_many_kittens(12, 13, True)
        'False'
    """
    return not (litterboxes >= kittens and catfood)
