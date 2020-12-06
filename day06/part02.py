f = open('input.txt', 'r')
data = f.read()
f.close

data_list = data.split("\n\n")
answer = 0

for line in data_list :
	matching = 0
	group = line.split('\n')
	group_size = len(group)
	fields = line.replace('\n', '')
	char_set = set(fields)
	for c in char_set :
		if fields.count(c) == group_size :
			matching = matching + 1
	answer = answer + matching

print(answer)
