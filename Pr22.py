import string
f = open("Pr22_names.txt","r")
names = []
for x in f:
 	names = x.split(',')
 	names.sort()
alphabet = {string.ascii_uppercase[i] : i+1 for i in range(0,26)}
alphabet['"'] = 0
ans = 0
for i in range(len(names)):
	name_temp = names[i]
	ans +=(i+1)*sum(alphabet[name_temp[j]] for j in range(len(name_temp)))
print(ans)