from Pr003 import ANS2
import math
from helper_functions import timer

@timer
def sum_square_diff(N: int) -> int:
    """Compute the difference between the summary of square values
    and the square of summary for the first <N> numbers .
    
    Parameters
    ----------
    `N` : int
        Upper limit of numbers needed for computation.
    
    Returns
    -------
    `res` : int
        Difference between aforementioned values.
    """
    sum_of_squares = sum(x**2 for x in range(1,N+1))
    square_of_sum = sum(x for x in range(1,N+1))
    square_of_sum = square_of_sum**2
    
    res = int(math.fabs(square_of_sum - sum_of_squares))
    return res

N1, ANS1 = 10, 2640
N2, ANS2 = 100, 25164150

if (__name__ == "__main__"):
    assert(sum_square_diff(N1) == ANS1) # for testing
    ans = sum_square_diff(N2)
    print(f"Problem 6 answer is {ans}")
    assert(ans == ANS2)