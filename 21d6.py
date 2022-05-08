with open("21d6.txt") as f:
    lfishes = f.read().strip().split(",")
print(lfishes)

newList = []
for _ in range(256):
    for lfish in lfishes:
        if int(lfish) == 0:
            newList.append(6)
            newList.append(8)

    for lfish in lfishes:
        if lfish != 0:
            newList.append(int(lfish) - 1)
        


    lfishes = newList
    newList = []

print(len(lfishes))
