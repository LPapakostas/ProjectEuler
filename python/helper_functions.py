from time import perf_counter 

def timer(func):
    """
    A decorator to calculate how long a function runs
    
    Parameters
    ----------
    `func` : callable
        The function being decorated.
        
    Returns
    -------
    `func` : callable
        The decorated function.
    """
    def wrapper(*args, **kwargs):
        start = perf_counter()
        res = func(*args, **kwargs)
        end = perf_counter()
        
        print(f"{func.__name__} took {round(end-start,4)} seconds to run")
        return res
    return wrapper