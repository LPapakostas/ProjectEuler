from helper_functions import timer

def divider_count(num: int) -> int:
    """ Helper function that returns the dividers
    count for a requested integer.
    """
    # Initialize dividers: 1 and <num> itselfs as factors.
    div_count = 2 
    limit = int(num**0.5) +1
    
    for i in range(2, limit):
        if( num%i == 0):
            div_count += 2 # add i and num/i as factors.
    return div_count # the number itself as a factor

@timer
def triangular_dividers_count(N: int) -> int:
    """Obtain the triangular number that has <N> 
    dividers.
    
    Notes
    -----
    The sequence of triangle numbers is generated 
    by adding the natural numbers.
    
    Parameters
    ----------
    N : `int` 
        Upper limit of dividers.
    
    Returns
    -------
    triag : `int`
        Triangular number that has over <N> dividers.
    """
    
    # Initialize values
    triag = 1
    current_num = 1
    condition = False
    count = 1
    
    while( not condition ):
        count = divider_count(triag)
        if (count > N):
            condition = True
            break
        current_num += 1
        triag += current_num
        
    return triag

if (__name__ == "__main__"):
    N1, ANS1 = 5, 28
    N2, ANS2 = 500, 76576500
    
    assert(triangular_dividers_count(N1) == ANS1)
    ans = triangular_dividers_count(N2)
    assert(ans == ANS2)
    print(f"Problem 12 answer is {ans}")
