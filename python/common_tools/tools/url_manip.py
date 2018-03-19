'''
Created on Mar 16, 2018

@author: marcel.zoll
'''

from urllib.parse import urlparse

def strip_decay_url(url):
    """ take only the basic hostname/path from url """
    up = urlparse(url)
    return up.hostname+up.path
