"""
Functions that measure time for functions to see performance of code
"""

"""
# TODO LIST

"""

"""
Importing extern modules
"""
import CTkMessagebox as CTkMessagebox
from functools import wraps
import time

"""
Importing internal modules
"""
#* IMPORTANT: DO NOT CHANGE THESE LINES
import os
import sys
sys.path = os.getcwd()
#* IMPORTANT: DO NOT CHANGE THESE LINES


def timeit(func):
    """
    Decorator function to measure the execution time of the input function.

    Use: 
    @timeit
        def my_function():
            print("Timed function")
    """
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper

def delay_decorator(seconds):
    """
    A decorator that adds a delay before executing the decorated function.
    
    Parameters:
    seconds (int): The number of seconds to delay execution.
    
    Returns:
    function: The decorated function with the added delay.

    Use:
    @delay_decorator(2)
        def my_function():
            print("Delayed function")
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator