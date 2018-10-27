import time
import math
lst = ''.join([str(x) for x in range(1,10)])

# correct
def is_pandigital_prod(x,p1,p2,lst):
    num_str = str(x)+str(p1)+str(p2)
    num_str = ''.join(sorted(num_str))
    if num_str == lst:
        return True
    return False

def product(x):
    p1,p2 = 1,x ; max_val = int(math.sqrt(x))+1
    for i in range(2,max_val):
        if ( x%i == 0) and (i<max_val):
            p1,p2 = int(x/i),i
        if(is_pandigital_prod(x,p1,p2,lst)):
            return True
    return False

start_time = time.time() ; N = 10**4
print(sum([ i for i in range(1,N) if product(i)]))
print('Time',time.time() - start_time,'seconds')