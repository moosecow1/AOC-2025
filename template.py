import time

# Needs "test.txt" and "input.txt"

def solve(input: str):
	pass

def main():
	with open("test.txt", "r", encoding="utf-8") as f:
		answer = solve(f.read())

		assert answer == 13

	with open("input.txt", "r", encoding="utf-8") as f:
		c = f.read()

		start = time.time_ns()
		
		answer = solve(c)

		print(f"Answer: {answer}\nTook: {(time.time_ns() - start) / 1000000}")

if __name__ == "__main__":
	main()
