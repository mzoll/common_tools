'''
Created on Sep 28, 2017

@author: marcel.zoll

define some commonly used units as multiplicative values, so that we wont have to guess what kind of factor they entail to standard definitions.
'''

class units:
    """ defines conversion factors between units
    Examples
    --------
    ```
    t = 1. * units.time.milliseconds
    print('t equal to ', t, units.time._native_name)
    ```
    """
    class time:
        seconds = 1.
        sec = 1
        minutes = 60.
        m = 60.
        hours = 3600.
        h = 3600.
        days = 24.*3600.
        d = 24.*3600.
        milliseconds = 1E-3
        ms = 1E-3
        microseconds = 1E-6
        mus = 1E-6
        nanoseconds = 1E-9
        ns = 1E-9
    class distance:
        meters = 1.
        m = 1.
        kilometers = 1E3 
        km = 1E3
    class weight:
        kilograms = 1.
        kg = 1.
        grams = 1E-3
        g = 1E-3
        tons = 1E3
        t = 1E3
    class factors:
        percent = 1E-2
        kilo = 1E3
        mega = 1E6
        giga =1E9
        tera = 1E12
        deci = 1E-1
        centi = 1E-2
        milli = 1E-3
        micro = 1E-6
        nano = 1E-9
    class abstract:
        money = 1.
    class money:
        Kronor = 1.
        SEK = 1.
        Dollar = 1.
        USD = 1.
        Euro = 1.
        EUR = 1.
    class _native_name:
        time = 'seconds'
        distance = 'meters'
        weight = 'kilogram'
        
        
def impl(value):
    """ gotten an implict unit value: multiply with this to just mark this variable as explicit unit dependent
    
    Examples
    --------
    ```
    t_ms = 1. * impl('milliseconds')
    print('t equal to ', t*units.time*milliseconds , units._native_name.time)
    ```
    """
    return(1.)
        