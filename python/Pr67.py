def triag(data):
	for i in range(len(data)-2,-1,-1):
		for j in range(i+1):
			data[i][j]+=max(data[i+1][j],data[i+1][j+1])
	return data[0][0]

f = open("Pr067_numbers.txt","r")
data = [[int(x) for x in line.split()] for line in f]
print(triag(data))
