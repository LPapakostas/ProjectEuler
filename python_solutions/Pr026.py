from helper_functions import timer

def compute_rep_cycle(num: int) -> int:
    """
    Compute the number of repetable digits 
    in 1/<num>.
    """
    
    cycle, divider = 0, 10
    check = (cycle < 1) or (num != 10)
    while (check):
        divider = (divider%num)*10
        cycle += 1
        check = (cycle < 1) or (divider != 10)
    return cycle
        

@timer
def find_max_repeatable_cycle(N: int) -> int:
    """
    Find the number in [1,N] that has the maximum
    repetition cycle of 1/<number>.
    """
    
    # Define constants 
    maximum_val, maximum_cycle = 0, 0
    for num in range(2,N):
        cycle_count = 1
        # Remove even numbers
        check = (num%2 !=0 ) and (num%5 != 0)
        if check:
            cycle_count = compute_rep_cycle(num)
        # Pinpoint the maximum values
        if (cycle_count > maximum_cycle):
            maximum_val, maximum_cycle = num, cycle_count
            
    return maximum_val

if (__name__ == "__main__"):
    N1, ANS1 = 10, 7
    N2, ANS2 = 1000, 983
    
    assert(ANS1 == find_max_repeatable_cycle(N1))
    ans = find_max_repeatable_cycle(N2)
    print(f"Problem 26 answer is {ans}")
    assert(ans == ANS2)
    
