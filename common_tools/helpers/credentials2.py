'''
Created on Jun 29, 2018

@author: marcel.zoll
'''

import os
import keyring

def credkey(cred_name, key, value=None, export=True):
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
    if value is not None:
        if export:
            os.environ[cred_key] = value
        return value

    value = os.environ.get(cred_key)
    if value is not None:
        return value

    value = keyring.get_password(cred_name, key)
    if value is not None:
        if export:
            os.environ[cred_key] = value
        return value

    value = input("enter value for {}:{}".format(cred_name, key))
    if value is not None:
        if export:
            os.environ[cred_key] = value
        return value

    raise Exception("Credential lookup failed")