#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Ensuring we have litterboxes for each kitten"""


def too_many_kittens(kittens, litterboxes, catfood):
    """ Ensures that each kitten has a litter box.

    Args:
        kittens (mixed): the number of kittens
        litterboxes (int): the number of available litterboxes
        catfood (bool): a bool representing whether or not any catfood exsists

    Returns:
        bool: all arguments in the boolean food statement

    Example:
        >>> too_many_kittens(12, 12, False)
        'True'
    """
    food = not (litterboxes >= kittens and catfood)
    return food
