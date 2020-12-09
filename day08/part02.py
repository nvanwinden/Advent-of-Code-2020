import copy

f = open('input.txt', 'r')
data = f.readlines()
f.close

data = [line.split() for line in data]

for instruction in data :
	check = 0
	if instruction[0] == 'jmp' :
		instruction[0] = 'nop'
		i = 0
		acc_count = 0
		new_data = copy.deepcopy(data)
		while i < len(new_data) :
			if len(new_data[i]) > 2 :
				instruction[0] = 'jmp'
				check = 1
				break
			if new_data[i][0] == 'nop' :
				new_data[i].append('executed')
				i += 1
			elif new_data[i][0] == 'acc' :
				new_data[i].append('executed')
				acc_count += int(new_data[i][1])
				i += 1
			elif new_data[i][0] == 'jmp' :
				new_data[i].append('executed')
				i += int(new_data[i][1])
		if check == 0 :
			answer = acc_count
			break

print(answer)
