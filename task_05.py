#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Setting default parameters"""


def defaults(my_required, my_optional=True):
    """ Logical comparison with .

    Args:
        my_required(bool): required parameter with not default value
        my_optional(bool): optional with a degfault value of true

    Returns:
        bool: logical comparison

    Example:
        >>> defaults(True)
        'True'
        >>> defaults(True, False)
        'False'
    """
    return my_optional is my_required
