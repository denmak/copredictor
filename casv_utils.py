# from multiprocessing import Pool
import urllib.request
import time
from functools import wraps


def timethis(func):
    '''
    Decorator that reports the execution time.


    '''

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print('func_name: ',func.__name__,' exec_time: ', end - start)
            return result
        except:
            print("error", *args, **kwargs)

    return wrapper


