#!/usr/bin/env python
# -*- coding: utf-8 -*-
"Docstring located here"


def defaults(my_required, my_optional=True):
    """This function determines something true or false.

    Args:
        my_optional(bool): has a default value of True
        my_required(bool): is a required parameter with no default value

    Returns:
        bool: wether or not a statement is true

    Examples:

        >>>defaults(True)
        True

        >>>defaults(True, False)
        False

        >>>defaults(False, False)
        True
    """
    return my_optional is my_required
