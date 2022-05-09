with open("21d6.txt") as f:
    ages = f.read().strip().split(",")
#print(lfishes)


for age in ages:
    ages[ages.index(age)] = int(age)

for day in range(80):
    newList = []
    for age in ages:
        if age == 0:
            newList.append(6)
            newList.append(8)
        else:
            newList.append(age - 1)

    ages = newList
    print(day + 1, ages)


print(len(ages))