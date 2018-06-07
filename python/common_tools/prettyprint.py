'''
Created on Mar 14, 2018

@author: marcel.zoll
'''

import pprint
_pp = pprint.PrettyPrinter(indent=4)

def print(*args):
    return _pp.pprint(args)
