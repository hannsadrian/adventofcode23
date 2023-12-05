def get_set_power(draws):
	required_red   = 0
	required_green = 0
	required_blue  = 0

	for draw in draws:
		for balls in draw:
			if balls[0] == "red" and required_red < balls[1]:
				required_red = balls[1]
			elif balls[0] == "green" and required_green < balls[1]:
				required_green = balls[1]
			elif balls[0] == "blue" and required_blue < balls[1]:
				required_blue = balls[1]

	return required_red * required_green * required_blue

with open("input.txt") as file:
	games = [] # structured like (id, [draw])

	while line := file.readline():
		game_part, draw_part = line.split(":", 2)
		game_id = int(game_part.split(" ")[-1])
		draws = []

		for d in draw_part.split(";"):
			d = d.replace(" ", "", 1)
			draw = []
			for color in d.split(", "):
				count, value = color.split(" ", 2)
				draw.append((value.replace("\n", ""), int(count)))
			draws.append(draw)

		games.append((game_id, draws))

	sum = 0
	for game in games:
		sum += get_set_power(game[1])

	print(sum)
