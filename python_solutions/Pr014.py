import time
N = 10**6
# The first value of dictonary contains the number for Collage 
# Series computation and the second one the steps of convergence
collage_chain = {1:1}
def fill_chain(n):
# Use recursive algorithm by the following lemma:
# 1) Collage(n) -> 1+Collage(n/2) , n is even
# 2) Collage(n) -> 2+Collage((3n+1)/2) , n is odd
	if n not in collage_chain:	
		if ( n%2 == 0):
			collage_chain[n] = 1 + fill_chain(int(n/2))
		else:
			collage_chain[n] = 2 + fill_chain(int( (3*n+1)/2 ) )
	return collage_chain[n] 

start = time.time() 
for i in range(N,1,-1):
# Compute Collage Series for all numbers 
	fill_chain(i)
# Find the maximum steps of convergence
longest_chain = max(collage_chain.values())
# Reverse the <collage_chain> dictionary in order to find 
# the number that contains the most steps
inv_dict = { value:key for key,value in collage_chain.items()}
print(inv_dict[longest_chain])
print("Time Evaluated :", time.time()-start," seconds")
