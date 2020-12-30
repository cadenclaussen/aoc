with open("19d1.txt") as f:
    a = f.read().strip().split("\n")
a = list(map(int, a))

total = 0
for num in a:
    total += (num // 3) - 2
print("Part 1: " + str(total))
