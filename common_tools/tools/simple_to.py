'''
Created on Sep 28, 2017

@author: marcel.zoll
'''

import numpy as np

def NoneToZero(arg):
    """ convert None to (int)0 ; helpful when used in mapping functions """
    return NoneTo(arg, 0)
    
def NoneTo(obj, target):
    """ convert a None-object to something else; helpful when used in mapping functions """
    if obj is None:
        return target
    return obj

def NanTo(obj, target):
    """ convert a NAN-float to something else; helpful when used in mapping functions """
    if np.isnan(obj):
        return target
    return obj
