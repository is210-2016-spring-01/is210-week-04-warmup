#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring"""


def defaults(my_optional=True, my_required):
    """A function with a default value.

    Args:
        my_optional(condition): First element that is defined. Default: True
        my_required (str, optional): Second element of the function

    Returns:
        str: All arguments is compared with commas

    Examples:

        >>> defaults(True)
        True

        >>> defaults(True, False)
        False

        >>> defaults(False, False)
        True
    """
    return my_optional is my_required

