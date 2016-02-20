#!usr/bin/env/python
# -*- uft code-8 -*-
"""Defining a function with three parameters."""

def too_many_kittens(kittens, litterboxes, catfood):
    """This function has three arguments.

    Args:
        kittens (int): the number of kittens
        litterboxes (int): the number of available litterboxes
        catfood (boolean): represents whether or not any catfood exists

    Return:
        mixed: value of a comparison statement

    Examples:

        >>>too_many_kittens(12, 12, False)
        True

        >>>too_many_kittens(13, 12, True)
        True

        >>>too_many_kittens(12, 13, True)
        False
    """
    return not (litterboxes >= kittens and catfood)
