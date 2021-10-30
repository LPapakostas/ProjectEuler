from helper_functions import timer

@timer
def compute_distinct_terms(N: int) -> int:
    """
    Compute distinct terms of `a^b` values
    for a,b in [2,N]. 
    """
    
    combinations = []
    
    for a in range(2,N+1):
        for b in range(2,N+1):
            combinations.append(a**b)
    
    distinct_terms = len(set(combinations))
    return distinct_terms 
            
            
if (__name__ == "__main__"):
    N1, ANS1 = 5, 15
    N2, ANS2 = 100, 9183
    assert(compute_distinct_terms(N1) == ANS1)
    ans = compute_distinct_terms(N2)
    assert(ans == ANS2)
    print(f"Problem 29 answer is: {ans}")
    