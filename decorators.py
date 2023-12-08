import time

def timing_decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Time taken to execute {func.__name__}: {elapsed_time} seconds")
            return result
        return wrapper