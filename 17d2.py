with open("17d2.txt") as f:
    a = f.read().strip().split("\n")

# print(a)
for i in range(len(a)):
    a[i] = list(map(int, a[i].split()))
# print(a)
total = 0
for line in a:
    total += max(line) - min(line)
print("Part 1: " + str(total))

total = 0
for line in a:
    for i in range(len(line)):
        for j in range(len(line)):
            if line[i] % line[j] == 0:
                if i == j:
                    continue
                else:
                    total += line[i] / line[j]
print("Part 2: " + str(total))
