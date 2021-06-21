import time
digits = "0123456789" 
check = [2,3,5,7,11,13,17]

def generate(lst):
	if (len(lst) == 1):
		return lst
	l = []
	for i in range(len(lst)):
		m = lst[i]
		rem_lst = lst[:i]+lst[i+1:]
		for x in generate(rem_lst):
			l.append(m+x)
	return l

def sub_divisibility(num):
	start = 2; stop = 4; flag = 0
	num = str(num)
	while (stop <= len(digits)) :
		sub_num = int(num[start-1:stop])
		if ( sub_num%check[flag] != 0) :
			return False
		start+=1 ; stop+=1 ; flag+=1
	return True

start = time.time() 
nums = set(generate(digits)) 
ans = sum([int(x) for x in nums if sub_divisibility(x)])
print(ans)
print("Time Evaluated:", time.time()-start,"seconds")

