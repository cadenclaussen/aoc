with open("21d4.txt") as f:
	a = f.read().strip().split()

import sys

order = [10,80,6,69,22,99,63,92,30,67,28,93,0,50,65,87,38,7,91,60,57,40,84,51,27,12,44,88,64,35,39,74,61,55,31,48,81,89,62,37,94,43,29,14,95,8,78,49,90,97,66,70,25,68,75,45,42,23,9,96,56,72,59,32,85,3,71,79,18,24,33,19,15,20,82,26,21,13,4,98,83,34,86,5,2,73,17,54,1,77,52,58,76,36,16,46,41,47,11,53]

def createBoard(a):
	counter = 0
	repeat = 0
	boards = []
	for item in a:
		if counter == 25:
			counter = 0
			repeat += 1
		if counter == 0:
			 boards.append([])
		boards[repeat].append(item)
		counter += 1 
	return boards


def isWin(l):
	if l[0] == "X" and l[1] == "X" and l[2] == "X" and l[3] == "X" and l[4] == "X":
		return True
	if l[5] == "X" and l[6] == "X" and l[7] == "X" and l[8] == "X" and l[9] == "X":
		return True
	if l[10] == "X" and l[11] == "X" and l[12] == "X" and l[13] == "X" and l[14] == "X":
		return True
	if l[15] == "X" and l[16] == "X" and l[17] == "X" and l[18] == "X" and l[19] == "X":
		return True
	if l[20] == "X" and l[21] == "X" and l[22] == "X" and l[23] == "X" and l[24] == "X":
		return True
	if l[0] == "X" and l[5] == "X" and l[10] == "X" and l[15] == "X" and l[20] == "X":
		return True
	if l[1] == "X" and l[6] == "X" and l[11] == "X" and l[16] == "X" and l[21] == "X":
		return True
	if l[2] == "X" and l[7] == "X" and l[12] == "X" and l[17] == "X" and l[22] == "X":
		return True
	if l[3] == "X" and l[8] == "X" and l[13] == "X" and l[18] == "X" and l[23] == "X":
		return True
	if l[4] == "X" and l[9] == "X" and l[14] == "X" and l[19] == "X" and l[24] == "X":
		return True
	if l[0] == "X" and l[6] == "X" and l[12] == "X" and l[18] == "X" and l[24] == "X":
		return True
	if l[4] == "X" and l[8] == "X" and l[12] == "X" and l[16] == "X" and l[20] == "X":
		return True
	return False

def calculateScore(a, num, index):
	sumOfOther = 0
	for item in a[index]:
		if item != "X":
			sumOfOther += int(item)
	return sumOfOther * int(num)

a = createBoard(a)

for number in order:
	for index in range(len(a)):
		for num in a[index]:
			if num == str(number):
				a[index][a[index].index(str(num))] = "X"
				if isWin(a[index]):
					print(index,"won.")
					a[index] = "XX"
					found = []
					for thing in a:
						if thing != "XX":
							found.append(thing)
							if a.index(thing) == 72:
								print(a)
					if len(found) == 1:
						score = calculateScore(a, num, a.index(thing))

print(a, score)


