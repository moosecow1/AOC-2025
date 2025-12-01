zeroCounter = 0
dial = 50

def parseInstruction(instruction: str):
	result = (False,0,)

	dirString = instruction[0]
	numString = instruction.lstrip(instruction[0])

	if dirString.lower() == "r":
		result = (True,0,)
    
	result = (result[0], int(numString))

	return result

def turn(right: bool, rotations: int):
	global zeroCounter
	global dial

	for i in range(rotations):
		if right:
			dial += 1
		else:
			dial -= 1

		if dial > 99:
			dial -= 100
		elif dial < 0:
			dial = 100 - (0 - dial)

		if dial == 0:
			zeroCounter += 1

	print(f"Dial: {dial}")

def iterateFile(instructions: list[str]):
	for instruction in instructions:
		parsed = parseInstruction(instruction)

		turn(parsed[0], parsed[1])

	print(f"It was 0, {zeroCounter} times")

def main():
	with open("input.txt", "r") as f:
		iterateFile(f.readlines())

if __name__ == "__main__":
	main()
