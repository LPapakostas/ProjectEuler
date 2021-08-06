from helper_functions import timer, is_prime


@timer
def get_prime(position: int) -> int:
    """Returns the <position>th prime number

Parameters
----------
`position`: int
            Prime number position, starting from 2.

    Returns
    -------
    Prime number of specific position
"""
# We start from 3 in order to increase our step by 2
    n_of_primes = 2
    prime_value = 3

    while(n_of_primes < position):
        prime_value += 2
        if is_prime(prime_value):
            n_of_primes += 1
    return prime_value


if (__name__ == "__main__"):
    N1, ANS1 = 6, 13
    N2, ANS2 = 10001, 104743

    assert(get_prime(N1) == ANS1)
    ans = get_prime(N2)
    print(f"Problem 7 answer is {ans}")
    assert(ans == ANS2)
