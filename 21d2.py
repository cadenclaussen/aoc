with open('21d2.txt') as f:
	a = f.read().strip().split("\n")
#print(a)
horizontal = 0
depth = 0
aim = 0
for item in a:
	x = item.split()
	if x[0] == "forward":
		horizontal += int(x[1])
		depth += aim * int(x[1])
	if x[0] == "down":
		aim += int(x[1])
	if x[0] == "up":
		aim -= int(x[1])
print(depth * horizontal)
 