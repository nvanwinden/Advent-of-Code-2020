f = open('input.txt', 'r')
data = f.readlines()
f.close

data = [int(num) for num in data]
data.append(0)
data.sort()

checked = {}

def get_arrangements(num) :

	range_lst = []
	num_lst = []
	total = 0
	
	if num == data[-1] :
		return 1
	if num in checked :
		return checked[num]
	r = range(num + 1, num + 4)
	for number in r :
		range_lst.append(number)
	j = 1
	while j < 4 and data.index(num) + j < len(data) :
		num_lst.append(data[data.index(num) + j])
		j += 1
	matches = list(set(num_lst).intersection(set(range_lst)))
	if len(matches) == 0 :
		return 0
	for i in matches :
		total = total + get_arrangements(i)
	checked[num] = total
	return total

answer = get_arrangements(0)
print(answer)
