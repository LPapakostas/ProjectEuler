import time
digits = "123456789"
up_limit = 10**5

def multiples(x):
	lst = []; i = 1
	while (len(lst) < len(digits)):
		lst+=list(str(x*i))
		i+=1
	test_digits = ''.join(lst)
	return test_digits
	'''
	if (''.join(sorted(test_digits)) == digits):
		return True
	return False
	'''

def is_pandigital(x):
	if (''.join(sorted(x)) == digits):
		return True
	return False

start = time.time() ; 
muls = set([multiples(x) for x in range(1,up_limit) ])
ans = [x for x in muls if is_pandigital(x)]
print(max(ans))
print("Time Evaluated:", time.time()-start,"seconds")
