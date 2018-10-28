def factorial(n):
    if n<2:
        return 1
    else:
        return n*factorial(n-1)

def is_sum_factorial(n,lst):
    n_str = str(n) ; s = 0 
    for i in range(len(n_str)):
        s+=lst[int(n_str[i])]
        if (s > n):
            return False
    if(s == n):
        return True
    return False
    
f_list =[ factorial(x) for x in range(0,10)]
N = 7*factorial(9)
print(sum([x for x in range(3,N) if is_sum_factorial(x,f_list)]))