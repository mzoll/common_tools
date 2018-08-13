'''
Created on Jun 13, 2018

@author: marcel.zoll
'''

import os, pickle

def diskpickle(obj, filepath, mode):
    """ write or read the pickle of an object to or from disc.
    
    Parameters
    ----------
    obj : object
        some picklable object
    filepath : str
        the path to where the object is to be written to or where it already has been written to
    mode : char 
        mode declaration ; 'w'=write, 'r'=read, 'e'=exist
    """
    if mode=='w':
        pickle.dump(obj, open(filepath, 'wb'))
    elif mode=='r':
        obj = pickle.load(open(filepath, 'rb'))
    elif mode=='e':
        if os.path.exists(filepath):
            obj = pickle.load(open(filepath, 'rb'))
        else:
            pickle.dump(obj, open(filepath, 'wb'))
    return obj
    