#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module does some comparisons"""

def too_many_kittens(kittens, litterboxes, catfood):

    """
    This Arguement compares litters boxes to kittens and catfood
    
    Args: Kittens
          Litterboxes
          Catfood

    Example:
    >>>too_many_kittens(12,14,True)
       False
        
    """
    value = not (litterboxes >= kittens and catfood)
    return value
