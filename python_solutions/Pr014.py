from helper_functions import timer

def collatz_chain_len(N : int) -> int:
    """Compute Collatz chain length for give number.
    
    Notes
    -----
    The Collatz sequence is defined for the set of positive integers:
		* n --> n/2 (n is even)
		* n --> 3n+1 (n is odd)
	All starting integers finish at 1.
    
    Parameters
    ----------
    N : `int`
		Number that Collatz chain length is computed.
	
	Returns
	-------
	Length of Collatz chain
    """
    # Check if Collatz chain length is already computed.
    if ( N in collatz_chain_ ):
        return collatz_chain_[N]
    
    if ( N == 1):
        return 1
    
    is_even = (N%2 == 0)
    if (is_even): 
	    return 1 + collatz_chain_len(N//2)
 
    return collatz_chain_len(3*N+1)

@timer
def find_max_collatz_chain_terms(N : int) -> int:
    """Helper function that finds the number that
    produces the longest chain in Collatz sequence.
    """
    global collatz_chain_ 
    collatz_chain_ = {}
    
    # Fill Collatz chain terms 
    for num in range(1,N):
        collatz_chain_[num] = collatz_chain_len(num)
    
    # Reverse dictionary in order to find the number
    # that produces the longest chain.    
    longest_chain = max(collatz_chain_.values())
    inv_dict = { value:key for key,value in collatz_chain_.items() }

    value = inv_dict[longest_chain]
    return value


if (__name__ == "__main__"):
    
    N, ANS = 1000000, 837799
    ans = find_max_collatz_chain_terms(N)
    print(f"Problem 14 answer is {ans}")
    assert(ans == ANS)
    