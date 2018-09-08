f = open("Pr13_numbers.txt","r")
data = list(f.readlines())
ans = sum(int((data[x])[:11]) for x in range(0,len(data)))
print(str(ans)[ :10])
