f = open('input.txt', 'r')
data = f.readlines()
f.close

data = [line.strip() for line in data]

def get_manhattan_dist() :
	ship_y = 0
	ship_x = 0
	wp_y = 1
	wp_x = 10

	for line in data :
		action, value = line[0], int(line[1:])
		if action == 'F' :
			ship_y += value * wp_y
			ship_x += value * wp_x
		elif action == 'N' :
			wp_y += value
		elif action == 'S' :
			wp_y -= value
		elif action == 'E' :
			wp_x += value
		elif action == 'W' :
			wp_x -= value
		elif action == 'L' :
			if value == 90 :
				wp_x, wp_y = -wp_y, wp_x
			if value == 180 :
				wp_x, wp_y = -wp_x, -wp_y
			if value == 270 :
				wp_x, wp_y = wp_y, -wp_x             
		elif action == 'R' :
			if value == 90 :
				wp_x, wp_y = wp_y, -wp_x
			if value == 180 :
				wp_x, wp_y = -wp_x, -wp_y
			if value == 270 :
				wp_x, wp_y = -wp_y, wp_x
		
	return (abs(ship_y) + abs(ship_x))

answer = get_manhattan_dist()
print(answer)
