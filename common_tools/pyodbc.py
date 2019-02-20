"""
Created on Feb 15, 2019

@author: marcel.zoll
"""

class PyodbcCredentials(object):
    def __init__(self, dsn, db, uid, pwd=None):
        self.dsn = dsn
        self.db = db
        self.uid = uid
        self.pwd = pwd

    def connectionString(self):
        s = "DSN={};DATABASE={};UID={};".format(self.dsn, self.db, self.uid, self.pwd)
        if self.pwd is not None:
            s += "PWD={};".format(self.pwd)
        return s


def pyodbcConnectionString(dsn, db, uid, pwd):
    return "DSN={};DATABASE={};UID={};PWD={}".format(dsn, db, uid, pwd)
