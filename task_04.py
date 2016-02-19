#!/usr/bin/env python
# -*- coding: utf-8 -*-
"Need more cats!"

def too_many_kittens(kittens, litterboxes, catfood):
    """Does some math with kittens, their food, and litterboxes.
	
	Args:
    	kittens(int): the number of kittens
	litterboxes(int): the (integer) number of avaliable litterboxes
	catfood(bool): a boolean representing wether or not any catfood exists
			
	Returns:
	Statement telling us wether or not we have at least 1 
	litterbox/catfood per kitten.
		
	Examples:
	
        	>>> too_many_kittens(12, 12, False)
            	True

		>>> too_many_kittens(13, 12, True)
		True

		>>> too_many_kittens(12, 13, True)
		False
		"""

    return not (litterboxes >= kittens and catfood)
