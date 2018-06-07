'''
Created on Mar 16, 2018

@author: marcel.zoll
'''

from urllib.parse import urlparse

def strip_decay_url(url):
    """ take only the basic hostname and path from url """
    up = urlparse(url)
    return up.hostname+up.path

def strip_domain_url(url):
    """ take only the basic hostname from url """
    up = urlparse(url)
    return up.hostname

def strip_path_url(url):
    """ take only the basic hostname from url """
    up = urlparse(url)
    return up.path