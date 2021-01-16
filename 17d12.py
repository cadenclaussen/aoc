from collections import defaultdict
with open("17d12.txt") as f:
    a = f.read().strip().split("\n")

connections = defaultdict(set)

for line in a:
	cur = line.split(" <-> ")
	pipe = cur[0]
	others = cur[1].split(", ")
	connections[pipe] |= set(others)

changed = True
while changed:
	changed = False
	for node in connections:
		added = True
		while added:
			added = False
			for j in connections[node]:
				before = len(connections[node])
				connections[node] |= connections[j]
				if before < len(connections[node]):
					changed = True
					added = True
					break

print("Part 1: " + str(len(connections["0"])))

seen = []
for pipe, cons in connections.items():
	if cons not in seen:
		seen.append(cons)
print("Part 2: ", len(seen))

