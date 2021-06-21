import time 

def abs_diff(x1,x2):
	if (x1 >= x2):
		return x1-x2
	else:
		return x2-x1

def is_pendagonal(x):
	# solve equation x = n(3n-1)/2 => 3n^2 -n -2x = 0 => 
	# n = (1+sqrt(1+24x))/6
	# so in order a number <x> is pendagonal, <n> must be integer so 
	# <n> modulo 6 must be equal to 0 
	return ( (1+(1+24*x)**0.5)%6 == 0.0 )
	
start = time.time()
k = 1 ; flag = True ; diff = 0
while(flag):
	for j in range(1,k):
		p_k = int(0.5*k*(3*k-1))
		p_j = int(0.5*j*(3*j-1))
		sum_p = p_k+p_j
		diff_p = abs_diff(p_k,p_j)
		if ( is_pendagonal(sum_p) and is_pendagonal(diff_p)):
			flag = False
			break
	k+=1
print(diff_p)
print("Time Evaluated:", time.time()-start,"seconds")
