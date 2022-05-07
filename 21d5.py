with open("21d5.txt") as f:
    lines = f.read().strip().split("\n")

coordinants = []
#print(lines)
for line in lines:
    data = line.split(" ")
    coordinants.append([data[0].split(","), data[2].split(",")])
print(coordinants)

