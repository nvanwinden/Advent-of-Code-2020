def get_num_bags(color, data) :
	hold_color = []
	color_names = []
	all_colors = []
	unique_colors = []

	for line in data :
		if color in line and line.index(color) != 0 :
			hold_color.append(line)
	for line in hold_color :
		name = line.split(' contain')
		name = name[0].replace(' bags', '')
		color_names.append(name)
	for color in color_names :
		all_colors.append(color)
		bag_colors = get_num_bags(color, data)
		all_colors += bag_colors
	for color in all_colors :
		if color not in unique_colors :
			unique_colors.append(color)
	return (unique_colors)

f = open('input.txt', 'r')
data = f.read()
f.close

data = data.splitlines()
answer = len(get_num_bags('shiny gold', data))
print(answer)
