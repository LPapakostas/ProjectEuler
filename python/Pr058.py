import time

def is_prime(num):
    if (num <= 2):
        return False
    for i in range(3,int(num**0.5)+1,2):
        if ( num%i == 0):
            return False
    return True

if (__name__ == "__main__"):
    start = time.time()
    n = 1 ; sides= 2*n +1; n_of_primes = 0
    while (n_of_primes/(2*sides-1) > 0.1 or n == 1):
        a_n = 4*n**2 - 2*n +1
        b_n = 4*n**2 + 1
        c_n = 4*n**2 + 2*n +1
        d_n = 4*n**2 + 4*n + 1
        diag_nums = list(map(is_prime,[a_n,b_n,c_n,d_n]))
        n_of_primes += len([x for x in diag_nums if x ])
        sides = 2*n +1 ; n+=1
    print(sides)
    print("Time evaluated",time.time()-start,"seconds")