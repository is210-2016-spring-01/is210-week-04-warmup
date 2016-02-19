#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module does a logical comparison"""

def defaults(my_required, my_optional=True):
 
    """ This function compares my_required with my_optional's default value;True

        Args:
            my_required
            my_optional=True
            
        Examples:

        >>> defaults(True)
        True

        >>> defaults(True, False)
        False

        >>> defaults(False, False)
        True
"""
    
    value = my_optional is my_required
    return value
    
    
