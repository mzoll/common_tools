'''
Created on Mar 16, 2018

@author: marcel.zoll
'''

import datetime as dt
import pandas as pd
import json

class JSON_Encoder(json.JSONEncoder):
    """ py3 implementation of an extended JSON encoder """
    def default(self, obj):
        """JSON serializer for objects not serializable by default json code"""
        if isinstance(obj, (dt.datetime, dt.date)):
            if isinstance(obj, pd.Timestamp):
                return obj.isoformat()
            return obj.isoformat(timespec='microseconds')
        return json.JSONEncoder.default(self, obj)


def json_serializer(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (dt.datetime, dt.date)):
        if isinstance(obj, pd.Timestamp):
            return obj.isoformat()
        return obj.isoformat(timespec='microseconds')
    raise TypeError ("Type %s not serializable" % type(obj))

