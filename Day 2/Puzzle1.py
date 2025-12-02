import math

total = 0

def check_invalid(id: str):
	global total

	if len(id) % 2 != 0:
		print(f"Uneven: {id}")
		return
	
	mid = len(id) // 2

	if id[:mid] == id[mid:]:
		total += int(id)
		print(f"Invalid: {id}")

def find_invalid_ids(ids: list[str]):
	global total

	for id in ids:
		first, last = id.split("-")

		for n in range(int(first), int(last)):
			check_invalid(str(n))
		
def main():
	with open("input.txt", "r") as f:
		find_invalid_ids(f.read().split(","))

	print(total)

if __name__ == "__main__":
	main()
