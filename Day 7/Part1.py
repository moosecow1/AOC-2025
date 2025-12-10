import time

test_answer = 21
splits = 0
used_spaces = []

def begin_beam(beam_pos, splitters, dimensions):
	global splits
	global used_spaces
	
	if beam_pos in used_spaces:
		return

	if 0 <= beam_pos[0] < dimensions[0] and 0 <= beam_pos[1] < dimensions[1]:
		used_spaces.append(beam_pos)
		
		if beam_pos in splitters:
			print(f"Split {beam_pos}")

			begin_beam((beam_pos[0]-1, beam_pos[1]), splitters, dimensions)
			begin_beam((beam_pos[0]+1, beam_pos[1]), splitters, dimensions)

			splits += 1
		else:
			begin_beam((beam_pos[0], beam_pos[1]+1), splitters, dimensions)

def map_splitters(lines):
	t = []

	for l in range(len(lines)):
		line = lines[l]

		for c in range(len(line)):
			char = line[c]

			if char == "^":
				t.append((c, l))

	return t

def solve(input: str):
	global splits

	splits = 0

	lines = input.splitlines()
	splitters = map_splitters(lines)
	dimensions = (len(lines[0]), len(lines))
	start = (dimensions[0] // 2, 0)

	begin_beam(start, splitters, dimensions)

	return splits

def main():
	with open("test.txt", "r", encoding="utf-8") as f:
		answer = solve(f.read())

		assert answer == test_answer

	with open("input.txt", "r", encoding="utf-8") as f:
		c = f.read()

		start = time.time_ns()
		
		answer = solve(c)

		print(f"Answer: {answer}\nTook: {(time.time_ns() - start) / 1000000}ms")

if __name__ == "__main__":
	main()
