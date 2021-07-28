# Decorator
from time import time

def performance(func):
    def wrapper_func(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'took {end - start} ms')
        return result
    return wrapper_func

# @logging
# @authenticated

@performance
def long_time():
    for i in range(0, 10000000):
        i*5

long_time()