from typing import Pattern
from helper_functions import timer

@timer
def compute_spiral_diagonal_sum(N: int) -> int:
    """
    """
    
    # NOTE: x = 1,..,size
    partial_sums = [1]
    
    # Up-Right numbers are x^2 
    up_right_sum = sum([ x*x for x in range(3, N+1, 2) ])
    partial_sums.append(up_right_sum)
    
    # Up-Left numbers are x^2 - x  + 1
    up_left_sum = sum([ x*x -x +1 for x in range(3, N+1, 2) ])
    partial_sums.append(up_left_sum)

    # Down-Right numbers are x^2 - 3(x-1)
    down_right_sum = sum([ x*x - 3*(x-1) for x in range(3, N+1, 2) ])
    partial_sums.append(down_right_sum)

    # Down-Left numbers are x^2 - 2(x-1) 
    down_left_sum = sum([ x*x - 2*(x-1) for x in range(3, N+1, 2) ])
    partial_sums.append(down_left_sum)
    
    result = sum(partial_sums)
    return result
    

if (__name__ == "__main__"):
    N1, ANS1 = 5, 101
    N2, ANS2 = 1001, 669171001
    assert(compute_spiral_diagonal_sum(N1) == ANS1)
    ans = compute_spiral_diagonal_sum(N2)
    assert(ans == ANS2)
    print(f"Problem 28 answer is {ans}")
