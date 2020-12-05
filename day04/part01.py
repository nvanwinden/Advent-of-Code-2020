f = open('input.txt', 'r')
data = f.read()
f.close

invalid = 0
total = 0

data_list = data.split("\n\n")

for line in data_list :
	fields = line.replace('\n', ' ')
	passport = dict(item.split(":") for item in fields.split(" "))
	total += 1
	if "byr" not in passport :
		invalid += 1
	elif "iyr" not in passport :
		invalid += 1
	elif "eyr" not in passport :
		invalid += 1				
	elif "hgt" not in passport :
		invalid += 1
	elif "hcl" not in passport :
		invalid += 1
	elif "ecl" not in passport :
		invalid += 1
	elif "pid" not in passport :
		invalid += 1

answer = total - invalid
print(answer)
