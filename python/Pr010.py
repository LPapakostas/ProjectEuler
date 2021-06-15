import time
from helper_functions import timer, sieve_of_eratosthenes

@timer
def prime_summation(N: int) -> int:
    """Helper function that returns the summation of
    all prime number up to input value.
    
    Note
    ----
    Uses `sieve_of_eratosthenes` method.
    """
    primes = sieve_of_eratosthenes(N)
    summary = sum(primes)
    return summary

if (__name__ == "__main__"):
    N1, ANS1 = 10, 17
    N2, ANS2 = 2000000, 142913828922
    
    assert(prime_summation(N1) == ANS1)
    ans = prime_summation(N2)
    print(f"Problem 10 answer is {ans}")
    assert(ans == ANS2)