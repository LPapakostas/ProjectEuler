import time

def triag(data):
	# Use of dynamic programming
	# Starting from bottom line, compute the max of two neigbour values
	# and add it to <j> element of upline
	for i in range(len(data)-2,-1,-1):
		for j in range(i+1):
			data[i][j]+=max(data[i+1][j],data[i+1][j+1])
	return data[0][0]

start = time.time()
f = open("Pr018_numbers.txt","r")
data = [[int(x) for x in line.split()] for line in f]
print(triag(data))
print("Time Evaluated :",time.time()-start," seconds")

