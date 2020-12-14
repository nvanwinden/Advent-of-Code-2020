f = open('input.txt', 'r')
data = f.readlines()
f.close

data.append('x' * len(data[0]))
data.insert(0, 'x' * len(data[0]))

grid_border = []

for line in data :
	grid_border.append('x' + line + 'x')

empty = 'L'
occupied = '#'

def check_sides(layout, y, x) :
	count = 0
	i, j = y, x
	while layout[i][j] != 'x' :
		i -= 1
		j -= 1
		if layout[i][j] == 'L' :
			break
		if layout[i][j] == '#' :
			count += 1
			break
	i, j = y, x
	while layout[i][j] != 'x' :
		i -= 1
		if layout[i][j] == 'L' :
			break
		if layout[i][j] == '#' :
			count += 1
			break
	i, j = y, x
	while layout[i][j] != 'x' :
		i -= 1
		j += 1
		if layout[i][j] == 'L' :
			break
		if layout[i][j] == '#' :
			count += 1
			break 
	i, j = y, x
	while layout[i][j] != 'x' :
		j -= 1
		if layout[i][j] == 'L' :
			break
		if layout[i][j] == '#' :
			count += 1
			break
	i, j = y, x
	while layout[i][j] != 'x' :
		j += 1
		if layout[i][j] == 'L' :
			break
		if layout[i][j] == '#' :
			count += 1
			break
	i, j = y, x
	while layout[i][j] != 'x' :
		i += 1
		j -= 1
		if layout[i][j] == 'L' :
			break
		if layout[i][j] == '#' :
			count += 1
			break
	i, j = y, x
	while layout[i][j] != 'x' :
		i += 1
		if layout[i][j] == 'L' :
			break
		if layout[i][j] == '#' :
			count += 1
			break
	i, j = y, x
	while layout[i][j] != 'x' :
		i += 1
		j += 1
		if layout[i][j] == 'L' :
			break
		if layout[i][j] == '#' :
			count += 1
			break
	return count

def check_grid(seat_layout) :
	new_layout = seat_layout.copy()
	y = 0
	for line in seat_layout :
		x = 0
		for char in line :
			if char == empty :
				count = check_sides(seat_layout, y, x)
				if count == 0 :
					new_layout[y] = new_layout[y][:x] + occupied + new_layout[y][x+1:]
			elif char == occupied :
				count = check_sides(seat_layout, y, x)
				if count >= 5 :
					new_layout[y] = new_layout[y][:x] + empty + new_layout[y][x+1:]
			x += 1
		y += 1
	return(new_layout)

def get_num_occupied(seat_layout) :
	count = 0
	for line in seat_layout:
		for char in line :
			if char == occupied :
				count += 1
	return (count)

def comp_layout() :
	seat_layout_1 = []
	seat_layout_2 = grid_border.copy()

	while seat_layout_1 != seat_layout_2 :
		seat_layout_1 = seat_layout_2.copy()
		seat_layout_2 = check_grid(seat_layout_1)

	return get_num_occupied(seat_layout_1)

answer = comp_layout()
print(answer)
