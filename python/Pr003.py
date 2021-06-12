from Pr002 import ANS1
from helper_functions import timer

@timer
def compute_max_prime_factor(N: int) -> int:
    """Does prime factorization for a given number
    and returns the largest factor.
    
    Notes
    -----
    Prime Factorization is finding which prime numbers multiply 
    together to make the original number.
    
    Parameters
    ---------- 
    `N` : int 
        Number that will be analyzed into prime factors.
    
    Returns
    -------
    `l_factor` : int
        The largest prime factor.
    """
    
    # Simultaniously divide by each number.
    # When surpasses the upper limit, the number N 
    # will contain the largest prime number
    pfactor = 2
    while ( N > pfactor**2 + 1):
        if (N%pfactor == 0):
            N = N/pfactor
            continue
        pfactor += 1

    l_factor = int(N)
    return l_factor

N1, ANS1 = 13195, 29
N2, ANS2 = 600851475143, 6857

if (__name__ == "__main__"):
    assert(compute_max_prime_factor(N1) == ANS1) # for testing only
    ans = compute_max_prime_factor(N2)
    print(f"Problem 3 answer is {ans}")
    assert(ans == ANS2)

    
