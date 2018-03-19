'''
Created on Mar 14, 2018

@author: marcel.zoll
'''


def pprint_dict(d):
    """ pretty print a dictionary """
    print( '{ '+',\n'.join([ k+': '+str(v) for k,v in d.items() ] )+' }')
    
def pprint_list(l):
    """ pretty print a dictionary """
    print( '[ '+',\n'.join([ str(i) for i in l ])+' ]'  )
    
def pprint(obj):
    """ pretty print object """
    if isinstance(obj, dict):
        pprint_dict(obj)
    elif isinstance(obj, list):
        pprint_list(obj)
    else:
        print(str(obj))