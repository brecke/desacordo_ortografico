from functools import wraps


def attribute(f):
    attrname = '_'+f.__name__
    
    @property
    def wrapper(instance, *args, **kwargs):
        if not hasattr(instance, attrname):
            value = f(instance, *args, **kwargs)
            setattr(instance, attrname, value)
        return getattr(instance, attrname)
        
    return wrapper
