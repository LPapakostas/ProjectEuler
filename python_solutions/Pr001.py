from helper_functions import timer


@timer
def find_sum(N: int) -> int:
    """Compute the summary of all multiples of 3 and/or 5
    below given number

    Parameters
    ----------
    `N` : int
        Upper limit of computation

    Returns
    -------
    `sum` : int
        Computed summary value
    """
    sum = 0
    for x in range(1, N):
        condition = (x % 3 == 0 or x % 5 == 0)
        if condition:
            sum += x
    return sum


if (__name__ == '__main__'):
    N1, ANS1 = 10, 23
    N2, ANS2 = 1000, 233168

    assert(find_sum(N1) == ANS1)  # just for testing
    ans2 = find_sum(N2)
    assert(ans2 == ANS2)
    print(f"Problem 1 answer is {ans2}")
