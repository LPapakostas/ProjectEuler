import time 
LIMIT = 1000 ; N_digits = 10

start = time.time()
ans = 0
for i in range(1,LIMIT):
	temp = str(i**i) ; ans = int(ans)
	if (len(temp) >= N_digits):
		temp = temp[-N_digits:]
	ans+=int(temp) ; ans = str(ans)
	if(len(ans) >= N_digits):
		ans = ans[-N_digits:]
print(ans)
print(time.time()-start)

