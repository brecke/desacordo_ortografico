
def return_tuple(f):
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        return result if isinstance(result, tuple) else (result,)
    return wrapper
