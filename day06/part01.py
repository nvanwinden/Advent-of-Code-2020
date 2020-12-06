f = open('input.txt', 'r')
data = f.read()
f.close

data_list = data.split("\n\n")
answer = 0

for line in data_list :
	fields = line.replace('\n', '')
	char_set = set(fields)
	answer = len(char_set) + answer

print(answer)
