with open("21d3.txt") as f:
	a = f.read().strip().split("\n")
#print(a)

import statistics
from statistics import mode

charecters = [[], [], [], [], [], [], [], [], [], [], [], []]

def concat(l):
    rg = 0
    v = None
    for item in l:
        if v == None:
            rg = str(item)
            v = 0
        else: 
            rg += str(item)
    return rg



for item in a:
    x = list(item)
    for g in range(0, 12):
        charecters[g].append(x[g])

gamma = []
epsilon = []

for g in range(0, 12):
    gamma.append((mode(charecters[g])))
    if mode(charecters[g]) == "0":
        epsilon.append("1")
    else:
        epsilon.append("0")

gamma = concat(gamma)
epsilon = concat(epsilon)
print(int(gamma, 2) * int(epsilon, 2))


