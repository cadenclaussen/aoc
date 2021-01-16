with open("17d9.txt") as f:
	a = f.read().strip()

in_garbage = False
depth = 0
pos = 0
score = 0
garbage_count = 0
while pos < len(a):
	if a[pos] == "!":
		pos += 2
		continue
	if in_garbage:
		if a[pos] == ">":
			in_garbage = False
	else:
		if a[pos] == "<":
			in_garbage = True
		elif a[pos] == "{":
			depth += 1
			score += depth
		elif a[pos] == "}":
			depth -= 1
	pos += 1

print("Part 1:", score)
