with open("21d1.txt") as f:
	a = f.read().strip().split("\n")
print(a)
greater = 0
isGreater = int(a[0]) + int(a[1]) + int(a[2])
pos = 1
print("First: " + str(isGreater))
for pos in range(1, len(a) - 2):
	n = int(a[pos]) + int(a[pos + 1]) + int(a[pos + 2])
	if n > isGreater:
		greater += 1
		print(str(n) +  ': Yes')
	else:
		print(str(n) +  ': No')
	isGreater = n

print("Number of greater: " + str(greater))
