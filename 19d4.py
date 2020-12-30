count = 0
for i in range(134564, 585159):
    cur = str(i)
    doesStayOrIncrease = [int(cur[j]) <= int(cur[j + 1]) for j in range(len(cur) - 1)]
    if not all(doesStayOrIncrease):
        continue
    isValid = False

    for j in range(len(cur) - 1):
        if cur[j] == cur[j + 1]:
            isValid = True
    if isValid:
        count += 1
print("Part 1: " + str(count))

count = 0
for i in range(134564, 585159):
    cur = str(i)
    doesStayOrIncrease = [int(cur[j]) <= int(cur[j + 1]) for j in range(len(cur) - 1)]
    if not all(doesStayOrIncrease):
        continue
    isValid = False

    for j in range(len(cur) - 3):
        if cur[j] == cur[j + 1] and not cur[j - 1] == cur[j] == cur[j + 1] and not cur[j] == cur[j + 1] == cur[j + 2] and not cur[j - 2] == cur[j - 1] == cur[j]:
            isValid = True
    if isValid:
        count += 1
print("Part 2: " + str(count))
