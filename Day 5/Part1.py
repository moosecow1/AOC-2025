import time

test_answer = 3

def solve(input: str):
	lines = input.splitlines()
	ranges = True
	fresh_count = 0
	range_table = []

	for y in range(len(lines)):
		if len(lines[y]) < 1:
			ranges = False
			range_table = list(set(range_table))
			continue

		if ranges:
			split = lines[y].split("-")
			left = int(split[0])
			right = int(split[1])

			range_table.append((left, right))

		else:
			fresh = False

			for rnge in range_table:
				try:
					if rnge[0] <= int(lines[y]) <= rnge[1]:
						fresh = True
				except:
					pass

			if fresh:
				fresh_count += 1

	return fresh_count

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
