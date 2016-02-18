#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""Task 5"""


def defaults(my_required, my_optional=True):
    """To check if one argument is equal to another argument.

    Args:
        my_required (bool): Arg to be assigned a True or False.
        my_optional (bool): Arg that is already assigned a True value.

    Returns:
        bool: returns True or False

    Examples:

        >>> defaults(True)
        'True'

        >>> defaults(False)
        'False'

        >>> defaults(False, False)
        'True'
    """
    return my_optional is my_required
