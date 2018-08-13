'''
Created on Jun 29, 2018

@author: marcel.zoll
'''

import os

def credkey(cred_name, key, value=None):
    """ for a specific credential-name tries to retrieve the UserName from the environment by the key <cred_name>_UN;
    if not found will promt the user for the interactive input which will be stored
    
    Parameters
    ----------
    cred_name : str
        name of the credentials to be retrieved
    cred_key : str
        name of the key to retrieve
    cred_value : str
        optional : provide the value directly (not recommended)
    """
    cred_key = (cred_name+'_'+key).upper()
    if value is None:
        value = os.environ.get(cred_key)
    if value is None:
        value = input("enter value for {}:{}".format(cred_name, key))
        os.environ[cred_key] = value
    return value
