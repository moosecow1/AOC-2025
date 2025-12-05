import time

# Needs "test.txt" and "input.txt"
# Change "test_answer"
test_answer = None

def solve(input: str):
	pass

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
