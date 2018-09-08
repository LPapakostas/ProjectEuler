f = open("Pr11_numbers.txt","r")
data = f.read()
data = list(data)
while('\n' in data):
    data.remove('\n')
while(' ' in data):
    data.remove(' ')

