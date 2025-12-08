import time

test_answer = 4277556

class Equation:
	def __init__(self, op: str, start: int, end: int):
		self.op = op
		self.start = start
		self.end = end
		self.nums = []

	def addNum(self, n: int):
		self.nums.append(n)

	def calc(self) -> int:
		if self.op == "+":
			return sum(self.nums)
		elif self.op == "*":
			t = 1

			for n in self.nums:
				t *= n

			return t
		else:
			print(f"unkown operator: {self.op}")

def solve(input: str):
	lines = input.splitlines()
	equations: list[Equation] = []
	i = 0
	opLine = lines[len(lines)-1]
	answer = 0

	while i < len(opLine)-1:
		operator = opLine[i]
		start = i

		i += 1

		while i < len(opLine) and opLine[i] in [" ", "\n", "\0"]:
			i += 1

		equations.append(Equation(operator, start, i))

	for e in equations:
		for i in range(len(lines)-1):
			# Extract number from line and add it to the equation

			strNum = lines[i][e.start:e.end]
			num = int(strNum)

			e.addNum(num)

		r = e.calc()

		answer += r

	return answer

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
