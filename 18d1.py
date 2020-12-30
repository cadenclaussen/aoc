with open("18d1.txt") as f:
    a = f.read().strip().split("\n")
a = list(map(int, a))
print(a)
print("Part 1: " + str(sum(a)))

seen = set()
total = 0
seen.add(total)
done = False
while not done:
    for num in a:
        total += num
        if total in seen:
            print("Part 2: " + str(total))
            done = True
            break
        else:
            seen.add(total)
