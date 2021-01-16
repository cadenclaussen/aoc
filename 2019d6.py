from collections import defaultdict
with open("2019d6.txt") as f:
    a = f.read().strip().split("\n")
# print(a)
direct_orbits = dict()

for line in a:
    orbitee, orbiter = line.split(")")
    direct_orbits[orbiter] = orbitee

answer = 0
HOME = "COM"
for planet in direct_orbits:
    pointer = direct_orbits[planet]
    count = 1
    while pointer != HOME:
        pointer = direct_orbits[pointer]
        count += 1
    answer += count

print("Part 1: " + str(answer))

you_path = []
pointer = direct_orbits["YOU"]
while pointer != HOME:
    pointer = direct_orbits[pointer]
    you_path.append(pointer)

santa_path = []
pointer = direct_orbits["SAN"]
while pointer not in you_path:
    pointer = direct_orbits[pointer]
    santa_path.append(pointer)

answer = you_path.index(santa_path[-1]) + 1 + len(santa_path)
print("Part 2: " + str(answer))
