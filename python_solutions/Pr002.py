from helper_functions import timer


@timer
def find_even_fibonacci_terms_sum(N: int) -> int:
    """Compute the summary of even-valued Fibonacci 
    terms, for a given upper limit

    Parameters
    ----------
    `N` : int
        Upper limit of computation

    Returns
    -------
    `sum` : int
        Computed summary value
    """
    f0, f1 = 1, 1  # Starting Fibonacci values
    sum = 0
    while (f1 < N):
        is_even = (f1 % 2 == 0)
        if is_even:
            sum += f1
        f0, f1 = f1, f1 + f0
    return sum


if (__name__ == '__main__'):
    N1, ANS1 = 100, 44
    N2, ANS2 = 4000000, 4613732

    assert(find_even_fibonacci_terms_sum(N1)
           == ANS1)  # Just for testing
    ans = find_even_fibonacci_terms_sum(N2)
    assert(ans == ANS2)
    print(f"Problem 2 answer is {ans}")
