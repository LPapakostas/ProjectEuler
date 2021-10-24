from helper_functions import timer, factorial


@timer
def find_lexicographical_perm(order: int, n_digits: int) -> int:
    """
    For given order, find the lexicographical permutations.
    """
    # Create "factorial" system base
    digits = [i for i in range(0, n_digits)]
    factorial_base = []
    for num in range(max(digits) + 1):
        factorial_base.append(factorial(num))
    factorial_base = factorial_base[::-1]

    # Initialize values for computation
    perm_digits = []
    num_to_div = order-1  # use zero indexing

    # Iterate through factorial base, divide given <order> number with
    # each factor, obtain and remove the divider-index element
    # until remainder is equal to zero. The produced digits
    # are the N-th lexicographical permutation
    for num in factorial_base:
        rem = int(num_to_div/num)
        num_to_div = num_to_div % num

        # Remove <rem> occurancy and add <rem> position digit on result
        perm_digits.append(str(digits[rem]))
        digits.pop(rem)

    res = int("".join(perm_digits))
    return res


if (__name__ == "__main__"):
    N_DIGITS = 10
    N, ANS = 1000000, 2783915460

    # find lexicographical numbers
    ans = find_lexicographical_perm(N, N_DIGITS)
    assert(ANS == ans)
    print(f"Problem 24 answer is {ans}")
