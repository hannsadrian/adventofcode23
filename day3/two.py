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

	iterator = re.finditer("(\d+|[*])", text)
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

	valid_coords: dict[tuple[int, int], list[int]] = {}
	for number in numbers:
		is_valid = False
		valid_coord: tuple[int, int]|None = None

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
						valid_coord = (line_num, line_col)

		if valid_coord is None:
			continue

		if valid_coords.get(valid_coord):
			valid_coords[valid_coord].append(number.value)
		else:
			valid_coords[valid_coord] = [number.value]

	sum = 0
	for v in valid_coords.values():
		if len(v) == 2:
			sum += v[0]*v[1]
	print(sum)
