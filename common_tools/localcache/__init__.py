

def get_localcache(cachetype, **kwargs):
    if cachetype == 'managed:
        from slmachine.externals.common_tools.localcache.managed import ManagedCache_Master
        cache = ManagedCache_Master()
    elif cachetype == 'memcached':
        from slmachine.externals.common_tools.localcache.memcached import MemcachedCache_Master
        cache = MemcachedCache_Master(**kwargs)
    elif cachetype == 'redis':
        from slmachine.externals.common_tools.localcache.redis import RedisCache_Master
        cache = RedisCache_Master(**kwargs)
    else:
        raise ValueError("Unknown cachetype : {}".format(cachetype))

    return cache