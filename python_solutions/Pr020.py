from helper_functions import timer,factorial

@timer
def factorial_digit_sum(N: int) -> int:
    """Computes sum of factorial digits for a given number.
    
    Parameters
    ----------
    N : `int`
		Number that the factorial sum is computed.
    
    Returns
    -------
    digit_sum : `int`
		Sum of computed factorial digits.
    """
    # Compute factorial and separate its digits.
    factorial_num = factorial(N)
    digits = [int(x) for x in str(factorial_num)]
    
    digit_sum = sum(int(d) for d in digits)
    return digit_sum

if (__name__ == "__main__"):
    
    N1, ANS1 = 10, 27
    N2, ANS2 = 100, 648
    
    assert(factorial_digit_sum(N1) == ANS1)
    ans = factorial_digit_sum(N2)
    assert(ans == ANS2)
    print(f"Problem 20 answer is {ans}")