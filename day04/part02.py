def valid_chars(string, charset) :
	for c in string :
		if c not in charset :
			return ("invalid")
		return ("valid")

f = open('input.txt', 'r')
data = f.read()
f.close

invalid = 0
total = 0
lst = []

data_list = data.split("\n\n")

for line in data_list :
	fields = line.replace('\n', ' ')
	passport = dict(item.split(":") for item in fields.split(" "))
	lst.append(passport)
	total += 1
	if "byr" not in passport :
		invalid += 1
		lst.remove(passport)
	elif "iyr" not in passport :
		invalid += 1
		lst.remove(passport)
	elif "eyr" not in passport :
		invalid += 1
		lst.remove(passport)		
	elif "hgt" not in passport :
		invalid += 1
		lst.remove(passport)
	elif "hcl" not in passport :
		invalid += 1
		lst.remove(passport)
	elif "ecl" not in passport :
		invalid += 1
		lst.remove(passport)
	elif "pid" not in passport :
		invalid += 1
		lst.remove(passport)

for item in lst :
	if (item['ecl'] != 'amb' and item['ecl'] != 'blu' and 
	item['ecl'] != 'brn' and item['ecl'] != 'gry' and 
	item['ecl'] != 'grn' and item['ecl'] != 'hzl' and 
	item['ecl'] != 'oth') :
		invalid += 1
	elif item['hcl'][0] != '#' or len(item['hcl']) != 7 or valid_chars(item['hcl'][-6:], "0123456789abcdef") == "invalid" :
		invalid += 1
	elif int(item['byr']) < 1920 or int(item['byr']) > 2002 :
		invalid += 1
	elif int(item['iyr']) < 2010 or int(item['iyr']) > 2020 :
		invalid += 1		
	elif int(item['eyr']) < 2020 or int(item['eyr']) > 2030 :
		invalid += 1
	elif item['pid'].isdigit() != True or len(item['pid']) != 9 :
		invalid += 1
	elif item['hgt'][-2:] != 'cm' and item['hgt'][-2:] != 'in' :
		invalid += 1
	elif item['hgt'][-2:] == 'cm' or item['hgt'][-2:] == 'in' :
		if item['hgt'][-2:] == 'cm' :
			num = item['hgt'][:-2]
			if int(num) < 150 or int(num) > 193 :
				invalid += 1
		elif item['hgt'][-2:] == 'in' :
			num = item['hgt'][:-2]
			if int(num) < 59 or int(num) > 76 :
				invalid += 1

answer = total - invalid
print(answer)
