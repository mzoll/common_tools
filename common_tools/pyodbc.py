'''
Created on July 9, 2018

@author: marcel.zoll
'''

import pyodbc

def pyodbcConnectString(dsn ,db, uid, pwd):
    """ compose a very simple pyodb connection string """
    return "DSN={};DATABASE={};UID={};PWD={}".format(dsn ,db , uid, pwd)