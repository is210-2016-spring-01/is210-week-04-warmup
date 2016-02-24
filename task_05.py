#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module contains a function that performs a boolean compare of two
   parameters, one of which has a default value."""


def defaults(my_required, my_optional=True):
    """This function determines if the two parameters are the same.

    Args:
        my_required (boolean): the required boolean parameter.
        my_optional (boolean): an optional second boolean parameter.

    Returns:
        boolean: indicates if the two paameters are the same.

    Examples:

        >>>too_many_kittens(5, 4, True)
        True

        >>> defaults(True)
        True

        >>> defaults(True, False)
        False

        >>> defaults(False, False)
        True
    """

    return my_optional is my_required
