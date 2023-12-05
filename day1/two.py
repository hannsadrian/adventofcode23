import re

textual_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open("input.txt") as file:
	sum = 0
	while line := file.readline():
		numbers = []


		for i, char in enumerate(line):
			if str(char).isnumeric():
				numbers.append((i, int(char)))

		for i, text in enumerate(textual_numbers):
			iterator = re.finditer(text, line)
			for element in iterator:
				numbers.append((element.start(), i+1))


		numbers.sort(key=lambda entry: entry[0])
		result = int(str(numbers[0][1]) + str(numbers[-1][1]))

		print(numbers, "->", result)

		sum += result
	print(sum)
