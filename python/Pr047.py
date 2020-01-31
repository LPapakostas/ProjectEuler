import time
LIMIT = 1000000
number_of_factors = 4

def factor_counter():
    # We need to find the number of factors for all numbers
    factor_counts = [0]*LIMIT
    for i in range(2,LIMIT):
        # if a number is prime,we add +1 to all its multiplies
        if (factor_counts[i] == 0 ): # prime number
            for j in range(2*i,LIMIT,i):
                factor_counts[j]+=1
    return factor_counts

def find(factor_counts):
    for i in range(2,LIMIT-number_of_factors-1):
        summary = sum([x for x in factor_counts[i:i+number_of_factors]])
        # Find the smallest number that has <number_of_factors> consecutive numbers
        # with <number_of_factors> distinct factors.
        if ( int(summary//number_of_factors) == number_of_factors ):
            return i
    return 0

def main():
    start = time.time()
    factor_counts = factor_counter()
    print(find(factor_counts))
    print("Time evaluated ", time.time()-start," seconds")

if (__name__ == '__main__'):
    main()
