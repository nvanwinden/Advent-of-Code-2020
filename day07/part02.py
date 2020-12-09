def get_num_bags(color):
	i = 0
	total = 0
    
	for line in data:
		if color + ' bags contain' in line :
			rule = line
	if 'no' in rule:
		return 1
	rule = rule.split(' contain')
	rule = rule[1].split()
	while i < len(rule):
		num = int(rule[i]) 
		color = rule[i + 1] + ' ' + rule[i + 2]
		total += num * get_num_bags(color)
		i += 4
	return total + 1

f = open('input.txt', 'r')
data = f.readlines()
f.close

answer = get_num_bags('shiny gold') - 1
print(answer)
