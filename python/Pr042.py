import time
alphabet = ("abcdefghijklmnopqrstuvwxyz").upper()
	
# Compute triangle numbers up to maximum letters word
def fill_chain(max_value):
	triangle_chain = []
	tr = 1; n =1
	while ( tr <= max_value):
		triangle_chain.append(tr)
		n+=1; tr = int(0.5*n*(n+1))
	return triangle_chain
	
# tranform letters to numbers ('A' = 1, .. 'Z' =26)
# and compute the sum of each word
def sum_of_letters(lst):
	sums = [0]*len(lst)
	for i in range(len(lst)):
		for c in lst[i]:
			sums[i] += (alphabet.index(c)+1)
	return sums

def find_triangle(lst,chain):
	count = 0  
	for i in range(len(lst)):
		if lst[i] in chain:
			count+=1
	return count
		
start = time.time()
# read data from file
f = open("Pr042_words.txt",'r')
data = f.read(); data = data.split(',')
data = [ x.strip('"') for x in data]
# find the longest word in order to pinpoint the upper limit
longest_word = max([len(x) for x in data])
# This is the upper limit
max_value = longest_word * (len(alphabet)+1)
# Compute triangle numbers tr(n) = 0.5*n*(n+1)
triangle_chain = set(fill_chain(max_value))
# Find numerical sum of each word
sums = sum_of_letters(data)
ans = find_triangle(sums,triangle_chain)
print(ans)
print("Time Evaluated :", time.time() - start, "seconds")

