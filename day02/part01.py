def valid_pass(data_list) :
	valid_pass = 0
	for line in data_list :
		wordsplit = line.split()
		range = wordsplit[0].split('-')
		range = [int(i) for i in range]
		lowest = min(range)
		highest = max(range)
		char = wordsplit[1][0]
		count = wordsplit[2].count(char)
		if count >= lowest and count <= highest :
			valid_pass = valid_pass + 1
	return (valid_pass)

f = open('input.txt', 'r')
data = f.read()
f.close

data_list = data.splitlines()
answer = valid_pass(data_list)
print(answer)
