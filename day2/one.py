TOTAL_RED   = 12
TOTAL_GREEN = 13
TOTAL_BLUE   = 14

def analyze_validity(draws):
	for draw in draws:
		for balls in draw:
			if balls[0] == "red" and balls[1] > TOTAL_RED:
				return False
			elif balls[0] == "green" and balls[1] > TOTAL_GREEN:
				return False
			elif balls[0] == "blue" and balls[1] > TOTAL_BLUE:
				return False

	return True

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
		if analyze_validity(game[1]) == True:
			sum += game[0]

	print(sum)
