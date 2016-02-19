#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module determines if two parameters match."""


def defaults(my_required, my_optional=True):
    """Defines a function that determines if the two parameters match.

    Args:
        my_optional (bool): optional parameter with a default value of True.
        my_required (bool): required parameter with no default value.

    Returns:
        bool: Whether or not the two parameters match.

    Examples:
        >>> defaults(True)
        True

        >>> defaults(True, False)
        False

        >>> defaults(False, False)
        True

    """
    return my_optional is my_required
