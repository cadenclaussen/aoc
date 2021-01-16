from collections import Counter
with open("18d2.txt") as f:
    a = f.read().strip().split("\n")

two_count = 0
three_count = 0
for line in a:
    cur = Counter(line)
    # print(cur)
    counts = set(cur.values())
    # print(counts)
    if 2 in counts:
        two_count += 1
    if 3 in counts:
        three_counts += 1
print("Part 1: " + str(two_count * three_count))
