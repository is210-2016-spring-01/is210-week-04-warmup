#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module contains a function that performs integer comparison with
   boolean operators."""


def too_many_kittens(kittens, litterboxes, catfood):
    """This function determines if we have at least one litterbox for each
       kitten and if we have some catfood.

    Args:
        kittens (int): the number of kittens.
        litterboxes (int): the number of available litterboxes.
        catfood (boolean): reflects whether or not any catfood exists.

    Returns:
        boolean: indicates if we have at least one litterbox for each kitten
        and if we have some catfood.

    Examples:

        >>>too_many_kittens(5, 4, True)
        True

        >>> too_many_kittens(10, 10, False)
        True

        >>> too_many_kittens(6, 7, True)
        False
    """

    return not (litterboxes >= kittens and catfood)
