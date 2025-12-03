import time

def get_joltages(s: str, joltage_digits: int=12) -> list[int]:
    joltages = []
    
    for l in s:
        l = l.strip()
        highestIndex = -1
        final = ""

        while len(final) < 12:
            start = highestIndex + 1
            reserveIndexCount = joltage_digits - (len(final) + 1)
            end = (len(l) - reserveIndexCount) # + 1

            biggest = -1

            for n in range(start,end):
                if int(l[n]) > biggest:
                    biggest = int(l[n])
                    highestIndex = n

            final += str(biggest)

        joltages.append(int(final))

        # print(final)

    return joltages

def main():
    with open("input.txt", "r") as f:
        content = f.readlines()

        start = time.time_ns()

        answer = sum(get_joltages(content))
        print(f"Answer: {answer}")

        print(f"Took {(time.time_ns() - start) / 1000000}ms")


if __name__ == "__main__":
    main()