def valid_pass(data_list) :
	valid_pass = 0
	for line in data_list :
		wordsplit = line.split()
		pos = wordsplit[0].split('-')
		pos = [int(i) for i in pos]
		pos_one = pos[0] - 1
		pos_two = pos[1] - 1
		char = wordsplit[1][0]
		if (wordsplit[2][pos_one] is char and wordsplit[2][pos_two] is not char 
		or wordsplit[2][pos_two] is char and wordsplit[2][pos_one] is not char) :
			valid_pass = valid_pass + 1
	return (valid_pass)

f = open('input.txt', 'r')
data = f.read()
f.close

data_list = data.splitlines()
answer = valid_pass(data_list)
print(answer)
