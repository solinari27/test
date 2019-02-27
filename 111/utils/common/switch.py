#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author: solinari 
@file: switch.py 
@time: 2018/11/04 
"""


class switch (object):
    """
    This class provides the functionality we want. You only need to look at
    this if you want to know how this works. It only needs to be defined
    once, no need to muck around with its internals.
    """
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args:  # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False