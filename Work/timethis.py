#timethis.py

def timethis(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__module__}.{func.__name__} took {end - start} seconds to run')
    return wrapper
