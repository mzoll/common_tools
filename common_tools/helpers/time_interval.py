'''
Created on Mar 16, 2018

@author: marcel.zoll
'''

import datetime as dt

from common_tools.units import units

def GetOffsetTimeInterval(dtime, offset= 0*units.time.seconds):
    '''return TrainingInterval tuple(startDate, endDate) of dtime(sec) duration and with offset(sec) from current time
    
    Parameters
    ----------
    dtime : float > 0
        extend of the interval in seconds 
    offset : float > 0
        offset in seconds
    
    Returns
    -------
    tuple of shape(2,) with (date_early, date_late)
    '''
    todaysDate = dt.datetime.now()
    return (todaysDate - dt.timedelta(seconds= offset+dtime),
            todaysDate - dt.timedelta(seconds= (offset)))


def GetSpecificTimeInterval(startdate, offset = 0*units.time.seconds):
    ''' return TimeInterval as touple(startDate, endDate)  extending nDays (pos or neg) from date
    
    Parameters
    ----------
    startdate : datetime.datetime
        the date to relatively compute the other date to
    offset : float
        extend of the interval in seconds
    
    Returns
    -------
    tuple of shape(2,) with (date_early, date_late)
    '''
    if startdate is None:
        return GetOffsetTimeInterval(abs(offset))
    if offset >= 0:
        return (startdate, startdate + dt.timedelta(seconds=offset))
    else:
        return (startdate - dt.timedelta(seconds=offset), startdate)

