#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module will create a new function for practice"""


def defaults(my_required, my_optional=True):
    """This function does a logical comparison and returns a boolean.

    Args:
        my_required (bool): Argument that is a required parameter \
        but has no default value.
        my_optional (bool): Argument that has a default value of True.

    Returns:
        bool: All arguments must return a boolean value of True or False.

    Examples:

        >>> defaults(True)
        True

        >>> defaults(True, Faulse)
        False

        >>> defaults(False, False)
        True
    """
    return my_optional is my_required
