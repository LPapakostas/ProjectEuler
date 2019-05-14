import time 
lower_lim = 286

def is_pendagonal(x):
	# solve equation x = n(3n-1)/2 => 3n^2 -n -2x = 0 => 
	# n = (1+sqrt(1+24x))/6
	# so in order a number <x> is pendagonal, <n> must be integer so 
	# <n> modulo 6 must be equal to 0 
	return ( (1+(1+24*x)**0.5)%6 == 0.0 )

def is_hexagonal(x):
	# solve equation x = n(2n-1) => 2n^2 -n -x = 0 => 
	# n = (1+sqrt(1+8x))/4
	# so in order a number <x> is hexagonal, <n> must be integer so 
	# <n> modulo 4 must be equal to 0 
	return ( (1+(1+8*x)**0.5)%4 == 0.0 ) 

start = time.time()
i = lower_lim ; flag = True ; num = 0
while(flag):
	num = int( 0.5*i*(i+1) )
	if ( is_pendagonal(num) and is_hexagonal(num) ):
		flag = False
		break
	i+=1
print(num)
print("Time Evaluated:", time.time()-start,"seconds")

