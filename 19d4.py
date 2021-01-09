count = 0
count2 = 0
for i in range(134564, 585159):
    cur = str(i)
    doesStayOrIncrease = \
    [int(cur[j]) <= int(cur[j+1]) for j in range(len(cur)-1)]
    if not all(doesStayOrIncrease):
        continue
    # print(doesStayOrIncrease)
    isValid = False

    for j in range(len(cur)-1):
        if cur[j] == cur[j+1]:
            isValid = True
    if isValid:
        count += 1

    #part 2
    isValid = False
    for j in range(10):
        num = str(j)
        if num * 2 in cur and num*3 not in cur:
            isValid = True
    if isValid:
        count2 += 1

print("part 1", count)
print("part 2", count2)
