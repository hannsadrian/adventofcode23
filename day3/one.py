import math
import re
from dataclasses import dataclass

@dataclass
class Number:
	value: int
	line: int
	start: int
	end: int

with open("input.txt") as file:
	text = file.read()
	lines = text.splitlines()
	line_length = len(lines[0])+1

	iterator = re.finditer("(\d+|[*#+$/=%@&-])", text)
	numbers: list[Number] = []
	symbols: dict[int, dict[int, str]] = {}

	for match in iterator:
		line_number = math.floor(match.start()/line_length)
		start = match.start() % line_length
		end = (match.end()-1) % line_length

		if match.group().isdigit():
			numbers.append(Number(
					value=int(match.group()),
					line=line_number,
					start=start,
					end=end
				))
		else:
			if symbols.get(line_number) is None:
				symbols[line_number] = {}
			symbols[line_number][start] = match.group()

	sum = 0
	for number in numbers:
		is_valid = False

		to_check = [
			list(range(number.start-1, number.end+2)),
			[number.start-1, number.end+1],
			list(range(number.start-1, number.end+2)),
		]

		for l, e in enumerate(to_check):
			line_num = number.line+l-1
			if line_num < 0:
				continue
			for line_col in e:
				if line_col < 0:
					continue
				if symbols.get(line_num) != None:
					if symbols[line_num].get(line_col) != None:
						is_valid = True

		if is_valid:
			sum += number.value

	print(sum)
