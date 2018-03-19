'''
Created on Dec 8, 2017

@author: marcel.zoll
'''

import datetime as dt
import numpy as np

import logging
logger = logging.getLogger('Stopwatch')


class Stopwatch(object):
    """ Stop the execution of a certain block of code
    Parameters
    ----------
    callobj : callable
        object to be called with `args` and `kwargs`
    args : arglist
        list of parameters on `callobj`
    args : arglist
        dictionary of arguments on `callobj`
     
    Examples
    --------
    import time
    Stopwatch(time.sleep, 1).clock(100)
    """
    def reset(self):
        self.laps = []
    def __init__(self, callobj, *args, **kwargs):
        if not callable(callobj):
            raise ValueError("passed callobj '%s' is not callable" % (callobj))
        self.callobj = callobj
        self.args = args
        self.kwargs = kwargs
        self.reset()    
    def runone(self):
        startstamp = dt.datetime.now()    
        self.result = self.callobj(*self.args, **self.kwargs)
        endstamp = dt.datetime.now()
        self.laps.append( (endstamp-startstamp).total_seconds() )
    def clock(self, ntimes = 1):
        self.reset()
        for i in range(ntimes):
            self.runone()
        
        logger.info("%d seconds for %d executions ( average: %f , median: %f )" % (np.sum(self.laps), len(self.laps), np.average(self.laps), np.median(self.laps)))
            
