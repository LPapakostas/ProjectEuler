from helper_functions import timer


@timer
def largest_palindrome_product(digits: int) -> int:
    """Computes the largest product between n-digit numbers
    that is palindrome.

    Notes
    -----
    A palindromic number is a number that remains the same 
    when its digits are reversed.

    Parameters
    ----------
    `digits` : int
        Number of digits.

    Returns
    -------
    `l_pali` : int
        Largest palindrome product.
    """
    start = 10 ** (digits-1)
    end = 10 ** digits
    l_pali = 0

    for n1 in range(start, end):
        for n2 in range(start, end):
            product = n1*n2
            is_palindrome = (str(product) == str(product)[::-1])
            if is_palindrome:
                l_pali = max(product, l_pali)

    return l_pali


if (__name__ == "__main__"):
    N1, ANS1 = 2, 9009
    N2, ANS2 = 3, 906609

    # just for testing
    assert(largest_palindrome_product(N1) == ANS1)
    ans = largest_palindrome_product(N2)
    print(f"Problem 4 answer is {ans}")
    assert(ans == ANS2)
