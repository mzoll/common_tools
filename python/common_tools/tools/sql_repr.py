'''
Created on Mar 16, 2018

@author: marcel.zoll
'''

import datetime as dt
import pandas as pd
import json
from .string_manip import squote

from .json_enc import JSON_Encoder

def sql_repr(val):
    """ give the sql *value* representation of a certain python value """
    if val is None:
        return "NULL"
    if isinstance(val, bool): #watch out: an assigned bool is also identified as a int
        return str(int(val))
    if isinstance(val, int) or isinstance(val, float):
        return (str(val))
    if isinstance(val, str):
        return squote(val)
    if isinstance(val, dt.datetime):
        if isinstance(val, pd.Timestamp):
            return squote(str(val))
        return squote(val.isoformat(sep=' ', timespec='milliseconds'))
        #except:
        #    print('die',type(val))
    else:
        return squote(json.dumps(val, cls=JSON_Encoder))
    
