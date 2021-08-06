from helper_functions import timer


@timer
def special_pythagorian_triplet(summary: int) -> int:
    """Finds product of a pythagorian triplet that 
    adds up to input value.

    Notes
    -----
    A Pythagorean triplet is a set of three natural numbers, 
    a < b < c, for which, a^2 + b^2 = c^2.

    Parameters
    ----------
    summary : `int`
                Number that a,b,c need to summarize.

        Returns
        -------
        product : `int`
                Product of founded a,b,c values.
    """
    product = 1  # dummy value
    b_flag = False
    for c in range(1, summary):
        # It is assured that always c > b
        for b in range(1, c):
            # Only need two loops --> Obtain <a> value
            # by substraction.
            a = summary - c - b
            pythagorian_condition = (c*c == b*b + a*a)
            if pythagorian_condition:
                product = a*b*c
                b_flag = True
                break
            else:
                continue
        if b_flag:
            break

    return product


if (__name__ == "__main__"):
    N, ANS = 1000, 31875000

    ans = special_pythagorian_triplet(N)
    print(f"Problem 009 answer is {ans}")
    assert(ans == ANS)
