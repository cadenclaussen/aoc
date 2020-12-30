with open("17d4.txt") as f:
    a = f.read().strip().split("\n")
# print(a)
count = 0
for line in a:
    cur = line.split(" ")
    # print(cur)
    if len(set(cur)) == len(cur):
        count += 1
print("Part 1: " + str(count))

count = 0
for line in a:
    cur = line.split(" ")
    # print(cur)
    isValid = True
    cur = list(map(set, cur))
    for i in range(len(cur)):
        if cur[i] in cur[i+1:]:
            isValid = False
            break
    if isValid:
        count += 1
print("Part 2: " + str(count))
