'''
Created on Mar 16, 2018

@author: marcel.zoll
'''


def GenEqualGroups(length, ngroups):
    ''' Generate a list of integers in a grouped sequence
    Parameters
    ----------
    length : int >0
        length of the generated series
    ngroups : int (0 ... length)
        number of groups to be generated
    
    Examples
    --------
    ```
    GenEqualGroups(10, 3)
    >>> [0,0,0,1,1,1,2,2,2,2]
    ```
    ''' 
    g = []
    nelpg = length / ngroups
    for i in range(ngroups):
        take_n = round(i*nelpg) - round((i-1)*nelpg)
        g.extend( [i]*take_n )
    if len(g) < length:
        g.extend( [ngroups-1 for i in range( length-len(g) ) ] )
    while len(g) > length:
        g.pop() 
    return g


def GenStrategicGroups(stratify, ngroups):
    ''' Generate a list of integers in a grouped sequence, 
    where grouped levels in stratifiy are not preserved.
    
    notice that stratify needs to be en-block
    '''
    g = []
    nelpg = float(len(stratify)) / ngroups
    
    prev_ = None
    grouped_idx = 0
    for i,s in enumerate(stratify):
        if i > (grouped_idx+1)*nelpg: 
            if s != prev_:
                grouped_idx += 1
        g.append(grouped_idx)
        prev_ = s
    return g
