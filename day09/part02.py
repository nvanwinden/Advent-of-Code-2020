f = open('input.txt', 'r')
data = f.readlines()
f.close

data = [int(i) for i in data]

def find_pairs(num, sublist) :
	for i in sublist :
		res = num - i
		if res in sublist :
			return 1
	return 0

def get_invalid_num(preamble) :
	sub = []
	k = 0
	i = preamble

	while i < len(data):
		j = 0
		while j < preamble :
			sub.append(data[j + k])
			j += 1
		res = find_pairs(data[i], sub)
		if res == 0 :
			return data[i]
		sub.clear()
		k += 1
		i += 1

invalid_num = get_invalid_num(25)

def get_weakness(invalid_num) :
	i = 0
	r_lst = []

	for num in data :
		res = 0
		j = i
		while res < invalid_num :
			res = data[j] + res
			r_lst.append(data[j])
			if res == invalid_num :
				return (min(r_lst) + max(r_lst))
			j += 1
		r_lst.clear()
		i += 1

answer = get_weakness(invalid_num)
print(answer)
