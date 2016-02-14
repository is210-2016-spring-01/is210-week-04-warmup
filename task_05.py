#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A module to determine are these the same."""


def defaults(my_required, my_optional=True):
    """Determines whether items are the same.

    Args:
        my_optional (bool): Defaults to True.
        my_requires (mixed): Any variable type.

    Returns:
        bool: Returns whether statement is True or False.

    Examples:

        >>> defaults(2)
        False

        >>> defaults(True)
        True
    """
    myvar = my_optional is my_required
    return myvar
