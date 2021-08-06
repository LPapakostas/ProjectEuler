from time import perf_counter


def timer(func):
    """A decorator to calculate how long a function runs.

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


def sieve_of_eratosthenes(limit: int) -> list:
    """Algorithm for finding all prime numbers up to any given limit. 

    Parameters
    ----------
    limit: `int`
        Upper limit for prime calculation.

    Returns
    -------
    primes: `list`
        All prime numbers from 2 through n
    """
    # Initialize a flag matrix for all numbers up to <limit> value.
    prime_flag = [True]*(limit+1)
    # initialize equal to smallest prime.
    prime_value = 2
    while(prime_value**2 < limit+1):
        if(prime_flag[prime_value] == True):
            # Enumerate the multiples of current prime by counting
            # in increments of current prime from 2*<prime_value> to
            # <limit> , and mark them in the list.
            for i in range(2*prime_value, limit+1, prime_value):
                prime_flag[i] = False
        # Increment the current <prime_value>
        prime_value += 1
    prime_flag[0], prime_flag[1] = False, False

    primes = [x for x in range(1, len(prime_flag)) if prime_flag[x]]
    return primes


def maximum(p: int, m: int) -> int:
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
    if (x < 2) or (x % 2 == 0):
        return False
    for i in range(3, int(x**(0.5))+1, 2):
        if (x % i == 0):
            return False
    return True


def factorial(n: int) -> int:
    """Returns the factorial of a given number.
    """
    if n < 2:
        return 1
    else:
        return n*factorial(n-1)
