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
    global dial

    if not right:
        rotations = -rotations

    dial += rotations
    
    while dial > 99 or dial < 0:
        if dial < 0:
            dial = 100 - (0 - dial)
        elif dial > 99:
            dial -= 100

    print(f"Dial: {dial}")

def iterateFile(instructions: list[str]):
    zeroCounter = 0

    for instruction in instructions:
        parsed = parseInstruction(instruction)

        turn(parsed[0], parsed[1])

        if dial == 0:
            zeroCounter += 1

    print(f"It was 0, {zeroCounter} times")

def main():
    with open("input.txt", "r") as f:
        iterateFile(f.readlines())

if __name__ == "__main__":
    main()
