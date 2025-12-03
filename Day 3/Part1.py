import time

def get_joltages(s: str) -> list[int]:
    joltages = []
    
    for l in s:
        highest = 0

        for x in range(len(l)):
            for y in range(len(l)-1-x):
                y += x + 1
                
                a = l[x]
                b = l[y]

                joltage = int(str(a) + str(b))

                if joltage > highest:
                    highest = joltage

            if x == len(l)-2:
                break

        joltages.append(highest)

    return joltages

def main():
    with open("input.txt", "r") as f:
        content = f.readlines()

        start = time.time_ns()

        joltages = get_joltages(content)
        total = sum(joltages)
        print(f"Answer: {total}")

        print(f"Took {(time.time_ns() - start) / 1000000}ms")


if __name__ == "__main__":
    main()