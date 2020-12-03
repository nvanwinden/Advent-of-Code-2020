def check_slope(data_list, right) :
	tree = '#'
	tree_count = 0
	first_line = 0
	pos = 0
	repeat = 1
	for line in data_list :
		while pos + 1 > len(line) :
			line = line * repeat
			repeat += 1
		if line[pos] is tree and first_line == 1 :
			tree_count += 1
		pos = pos + right
		first_line = 1
	return (tree_count)

f = open('input.txt', 'r')
data = f.read()
f.close

data_list = data.splitlines()
answer = check_slope(data_list, 3)
print(answer)
