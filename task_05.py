#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Defaults"""


def defaults(my_required, my_optional=True):

    """This function tests if the default coincides with the correct
    parameter

    Arguments:
        my_required(Boolean): This parameter does not have a default value.
        my_optional(Boolean): This parameter has the value of True.

    Example:
        >>> defaults(True)
        True
        >>> defaults(True, False)
        False
        >>> defaults(False, False)
        True

    """

    return my_optional is my_required
