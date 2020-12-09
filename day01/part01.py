def twentytwenty(data_list) :
	data_list = [int(i) for i in data_list]
	for num in data_list :
		for num1 in data_list :
			numsum = num + num1
			if numsum == 2020 :
				answer = num * num1
				return (answer)

f = open('input.txt', 'r')
data = f.read()
f.close()

data_list = data.splitlines()
answer = twentytwenty(data_list)
print(answer)
