import math , time

start = time.time() ; N = 100
sum_of_squares = sum(x**2 for x in range(1,N+1))
square_of_sum = sum(x for x in range(1,N+1))
print(int(math.fabs(square_of_sum**2 - sum_of_squares)))
print(time.time() - start,"seconds")
