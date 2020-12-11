f = open('input.txt', 'r')
data = f.readlines()
f.close

data = [int(num) for num in data]
data.append(0)
data.sort()
data.append(data[-1] + 3)

i = 0
count_one = 0
count_three = 0

while i < len(data) - 1 :
	count = data[i + 1] - data[i]
	if count == 1 :
		count_one += 1
	elif count == 3 :
		count_three += 1 
	i += 1

answer = count_one * count_three
print(answer)
