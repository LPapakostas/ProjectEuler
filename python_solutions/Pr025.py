from helper_functions import timer


@timer
def fibonacci_index(digit_num: int) -> int:
    """Returns the index of Fibonacci number that 
    has the same number of digits as input

    Parameters
    ----------
    digit_num : `int`
        Given number of digits
    """
    # Initialize fibonacci terms
    fn1, fn2 = 1, 1
    index = 2
    condition = not (len(str(fn2)) == digit_num)

    while(condition):
        fn1, fn2 = fn2, fn1+fn2
        index += 1
        condition = not (len(str(fn2)) == digit_num)

    return index


if (__name__ == "__main__"):
    N1, ANS1 = 3, 12
    N2, ANS2 = 1000, 4782

    assert(ANS1 == fibonacci_index(N1))
    ans = fibonacci_index(N2)
    print(f"Problem 25 answer is {ans}")
    assert(ans == ANS2)
