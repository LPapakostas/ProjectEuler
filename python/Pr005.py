from helper_functions import timer, is_prime
from math import log10, floor

@timer
def prime_lcm_product(N: int) -> int:
    """Table method prime factorization using Least Common Multiple.
    
    Notes
    -----
    Find the least common multiple is equivalent to find the smallest
    divisible number by each of [1,<N>] numbers.
    
    Parameters
    ----------
    N : `int`
		Upper limit of numbers.
  
	Returns
	-------
	product : `int`
		Smallest divisible number.
    """
    # Create a table for available prime number up to <N> value
    primes = [x for x in range(1,N+1) if is_prime(x)]
    
    # Initialize helper variables
    product = 1
    curr_idx = 0
    check_flag = True
    LIMIT = int(N**0.5)
    
    # Write each number as prime[idx] ^ alpha[idx]
    while ( curr_idx < len(primes) ):
        alpha = 1
        if (check_flag):
            if (primes[curr_idx] <= LIMIT):
                # For a given prime, alpha value determinated this way.
                alpha = floor( log10(N) / log10(primes[curr_idx]) )
            else:
                check_flag = False
        product *= primes[curr_idx]**alpha
        curr_idx += 1
	
    return product
	
if (__name__ == "__main__"):
    N, ANS = 20, 232792560
    ans = prime_lcm_product(N)
    print(f"Problem 005 answer is {ans}")
    assert(ans == ANS)