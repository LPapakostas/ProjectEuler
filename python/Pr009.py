import time
SUM = 1000

def pythagorian_tri(N):
# Only need 2 loops in order to find a triplet
# because <a> side can be obtained by N = a + b +c
	for c in range(1,N):
	# With this loop, it is assured that always c > b
		for b in range(1,c):
			a = N-(c+b) 					
			if (c*c == a*a+b*b):
				return a*b*c

start = time.time() 
print(pythagorian_tri(SUM))
print("Time Evaluated :", time.time()-start,"seconds")

    
