from time import time

def performance(func):
    def wrapper_func(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'took: {end - start}')
        return result
    return wrapper_func

@performance
def long_time():
    print('long_time1 execution')
    for i in range(10000000):
        i*5

@performance
def long_time2():
    print('long_time2 execution')
    for i in list(range(10000000)):
        i*5

long_time()
long_time2()