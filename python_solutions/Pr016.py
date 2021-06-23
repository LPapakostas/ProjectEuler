from helper_functions import timer

@timer
def sum_pow_two(pow: int) -> int:
    """Computes the summary of 2 raised in given power.
    
    Parameters
    ----------
    pow : `int`
        Power that 2 is raised.
    
    Returns
    -------
    digit_sum : `int`
        Digit summary of 2 raised in given power.  
    """
    pow_digits = list(str(2**pow))
    digit_sum = 0
    for digit in pow_digits:
        digit_sum += int(digit)
    
    return digit_sum

if (__name__ == "__main__"):
    N1, ANS1 = 15, 26 
    N2, ANS2 = 1000, 1366
    
    assert(sum_pow_two(N1) == ANS1)
    ans = sum_pow_two(N2)
    assert(ans == ANS2)
    print(f"Problem 16 answer is {ans}")