with open("17d5.txt") as f:
    a = f.read().strip().split("\n")
a = list(map(int, a))
# print(a)
temp = a.copy()

pos = 0
jumps = 0
while 0 <= pos < len(a):
    cur = pos
    pos += a[pos]
    a[cur] += 1
    jumps += 1
print("Part 1: " + str(jumps))

a = temp.copy()
pos = 0
jumps = 0
while 0 <= pos < len(a):
    cur = pos
    pos += a[pos]
    if a[cur] >= 3:
        a[cur] -= 1
    else:
        a[cur] += 1
    jumps += 1
print("Part 2: " + str(jumps))
