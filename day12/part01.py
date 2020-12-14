f = open('input.txt', 'r')
data = f.readlines()
f.close

data = [line.strip() for line in data]

def change_dir(action, angle, value) :
	if action == 'L' :
		angle -= value
	elif action == 'R' :
		angle += value
	return (angle)

def get_manhattan_dist(angle) :
	y = 0
	x = 0
	for line in data :
		action, value = line[0], int(line[1:])
		angle = angle % 360
		if action == 'N' :
			y += value
		elif action == 'S' :
			y -= value
		elif action == 'E' :
			x += value
		elif action == 'W' :
			x -= value
		elif action == 'L' or action == 'R' :
			angle = change_dir(action, angle, value)
		elif action == 'F' :
			if angle == 0 :
				y += value
			elif angle == 180 :
				y -= value
			elif angle == 90 :
				x += value
			elif angle == 270 :
				x -= value
	return (abs(y) + abs(x))

answer = get_manhattan_dist(90)
print(answer)
