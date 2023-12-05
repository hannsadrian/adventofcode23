with open("input.txt") as file:
	sum = 0
	while line := file.readline():
		numbers = []
		for char in line:
			if str(char).isnumeric():
				numbers.append(int(char))
		result = int(str(numbers[0]) + str(numbers[-1]))
		sum += result
	print(sum)
