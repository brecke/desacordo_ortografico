
def return_tuple(f):
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        if result==None:
            return result
        if isinstance(result, tuple):
            return result
        return (result,)
    return wrapper
