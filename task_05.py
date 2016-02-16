#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module compares to values to see if they are the same"""


def defaults(my_required, my_optional=True):
    """A function to see if there's at least one litterbox per kitten and food.

    Args:
        my_optional (bool, default=True): First comparison value (Optional).
        my_required (mixed): Argument to test against my_optional.

    Returns:
        bool: Whether or not two variables are the same.

    Examples:

        >>> defaults(True)
        True

        >>> defaults(True, False)
        False
    """
    return my_optional is my_required
