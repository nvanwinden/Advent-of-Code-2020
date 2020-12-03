def check_slope(data_list, right, down) :
	tree = '#'
	tree_count = 0
	first_line = 0
	pos = 0
	repeat = 1
	row_count = 0
	for line in data_list :
		if row_count % down == 0 and first_line == 1 :
			pos = pos + right
			while pos + 1 > len(line) :
				line = line * repeat
				repeat += 1
			if line[pos] is tree :
				tree_count += 1
		first_line = 1
		row_count += 1
	return (tree_count)

f = open('input.txt', 'r')
data = f.read()
f.close

data_list = data.splitlines()
a = check_slope(data_list, 1, 1)
b = check_slope(data_list, 3, 1)
c = check_slope(data_list, 5, 1)
d = check_slope(data_list, 7, 1)
e = check_slope(data_list, 1, 2)
print(a * b * c * d * e)
