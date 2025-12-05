import time

test_answer = 13

def solve(input: str):
	lines = input.split()
	accessible_rolls = 0

	for y, line in enumerate(lines):
		for x, char in enumerate(line):
			if char != "@":
				continue

			rolls = 0

			for o_x in range(-1,2):
				for o_y in range(-1, 2):
					coord = (x+o_x, y+o_y)

					if coord == (x,y) or coord[0] < 0 or coord[1] < 0 or coord[0] > len(line)-1 or coord[1] > len(lines)-1:
						continue

					if lines[coord[1]][coord[0]] == "@":
						rolls += 1

			if rolls < 4:
				accessible_rolls += 1

	return accessible_rolls

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
