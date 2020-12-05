f = open('input.txt', 'r')
data = f.read()
f.close

data_list = data.split()
id_lst = []

for boardingpass in data_list :
	row = 127
	col = 7
	seat_id = 0
	if boardingpass[0] == 'F' :
		row -= 64
	if boardingpass[1] == 'F' :
		row -= 32
	if boardingpass[2] == 'F' :
		row -= 16
	if boardingpass[3] == 'F' :
		row -= 8
	if boardingpass[4] == 'F' :
		row -= 4
	if boardingpass[5] == 'F' :
		row -= 2
	if boardingpass[6] == 'F' :
		row -= 1
	if boardingpass[7] == 'L' :
		col -= 4 
	if boardingpass[8] == 'L' :
		col -= 2
	if boardingpass[9] == 'L' :
		col -= 1
	seat_id = row * 8 + col
	id_lst.append(seat_id)

answer = max(id_lst)
print(answer)
