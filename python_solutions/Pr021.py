from helper_functions import timer


@timer
def amicable_number_sum(N: int) -> int:
    """
    Find the sum of amiciable numbers given a specific upper limit.

    Notes
    -----
    Let d(n) be defined as the sum of proper divisors of <n> 
    (numbers less than <n> which divide evenly into <n>).

    If d(a) = b and d(b) = a, where a ≠ b, a and b are called amicable numbers.
    """
    amicable_numbers = set()

    for num_a in range(N+1):
        num_b = sum_of_gcd(num_a)
        is_amicable = (num_a == sum_of_gcd(num_b) and num_b != num_a)
        if is_amicable:
            amicable_numbers.add(num_a)
            amicable_numbers.add(num_b)

    amiciable_sum = sum(list(amicable_numbers))
    return amiciable_sum


def sum_of_gcd(x: int) -> int:
    """
    Helper function that, given a number, it computes
    the summary of each greatest common divisors.
    """
    # Initialize sum with <1>, since every nunber
    # has one as divisor
    gcd_sum = 1  # 1
    limit = int(x**0.5) + 1

    # Find divisors until sqrt(x) because
    # if one divisor is i, the other is x/i
    for i in range(2, limit):
        if (x % i == 0):
            gcd_sum += int(x/i) + i

    return gcd_sum


if (__name__ == "__main__"):
    N, ANS = 10000, 31626

    ans = amicable_number_sum(N)
    print(f"Problem 21 answer is {ans}")
    assert(ans == ANS)
