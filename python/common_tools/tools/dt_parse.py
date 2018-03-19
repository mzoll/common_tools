'''
Created on Mar 16, 2018

@author: marcel.zoll
'''

import datetime as dt


def datetime_from_string(dtstring):
    try:
        return datetime_from_plainstring(dtstring)
    except:
        pass
    try:
        return datetime_from_isostring(dtstring)
    except:
        pass
    raise Exception("parsing '%s' as datetime.datetime have failed" % (dtstring))

def datetime_from_plainstring(dtstring): #FIXME change name to datetime_from_sqlstring
    try: #if re.match("....-..-.. ..:..:..", string):
        return dt.datetime.strptime(dtstring, '%Y-%m-%d %H:%M:%S')
    except:
        pass
    try: #if re.match("....-..-.. ..:..:..[.]......", string):
        return dt.datetime.strptime(dtstring, '%Y-%m-%d %H:%M:%S.%f')
    except:
        pass
    raise Exception("parsing '%s' as datetime.datetime have failed" % (dtstring))

def datetime_from_isostring(dtstring):
    #if re.match("....-..-..T..:..:..[.]......", string):
    try:
        return dt.datetime.strptime(dtstring, '%Y-%m-%dT%H:%M:%S.%f')
    except:
        pass
    try:
        return dt.datetime.strptime(dtstring, '%Y-%m-%dT%H:%M:%S')
    except:
        pass
    raise Exception("parsing '%s' as datetime.datetime have failed" % (dtstring))
