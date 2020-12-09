f = open('input.txt', 'r')
data = f.readlines()
f.close

data = [line.split() for line in data]

acc_count = 0
i = 0
while i < len(data) :
	if len(data[i]) > 2 :
		break
	if data[i][0] == 'nop' :
		data[i].append('executed')
		i += 1
	elif data[i][0] == 'acc' :
		data[i].append('executed')
		acc_count += int(data[i][1])
		i += 1
	elif data[i][0] == 'jmp' :
		data[i].append('executed')
		i += int(data[i][1])
answer = acc_count
print(answer)
