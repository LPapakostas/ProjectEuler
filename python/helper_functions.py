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

def maximum(p: int,m: int) -> int:
    """Returns maximum value between two numbers.
    """
    if p > m:
        return p
    return m

def is_prime(x: int) -> bool:
    """Returns True if for a prime number.
    """
    if (x == 2):
        return True
    if (x<2) or (x%2 == 0) :
        return False
    for i in range(3,int(x**(0.5))+1,2):
        if (x%i == 0):
            return False
    return True