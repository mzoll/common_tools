'''
Created on Sep 28, 2017

@author: marcel.zoll
'''

import numpy as np

def NoneToZero(arg):
    """ convert None to (int)0 """
    return NoneTo(arg, 0)
    
def NoneTo(obj, target):
    if obj is None:
        return target
    return obj

def NanTo(obj, target):
    if np.isnan(obj):
        return target
    return obj
