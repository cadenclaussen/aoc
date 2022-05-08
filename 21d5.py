with open("21d5.txt") as f:
    lines = f.read().strip().split("\n")

def printPlane(plane):
    for y in plane:
        for x in y:
            if x == "0 ":
                x = ". "
            print(x, end="")
            if x == ". ":
                x = "0 "
        print("")

coordinants = []
#print(lines)
for line in lines:
    data = line.split(" ")
    coordinants.append([data[0].split(","), data[2].split(",")])

#print(coordinants)

maximum = 0
for coordinant in coordinants:
    x1 = int(coordinant[0][0])
    x2 = int(coordinant[1][0])
    y1 = int(coordinant[0][1])
    y2 = int(coordinant[1][1])
    maximum = max(maximum, x1, x2, y1, y2)
board = maximum + 2

plane = []
for y in range(board):
    plane.append([])
    for x in range(board):
        plane[y].append("0 ")


printPlane(plane)
def checkHorizVert(coordinants, plane):
    for coordinant in coordinants:
        x1 = int(coordinant[0][0])
        x2 = int(coordinant[1][0])
        y1 = int(coordinant[0][1])
        y2 = int(coordinant[1][1])
        if x1 == x2:

            if y1 > y2:
                for i in range(y1 - y2 + 1):
                    plane[y2 + i][x1] = str(int(plane[y2 + i][x1]) + 1) + " "

            if y2 > y1:
                for i in range(y2 - y1 + 1):
                    plane[y1 + i][x1] = str(int(plane[y1 + i][x1]) + 1) + " "

        elif y1 == y2:

            if x1 > x2:
                for i in range(x1 - x2 + 1):
                    plane[y1][x2 + i] = str(int(plane[y1][x2 + i]) + 1) + " "

            if x2 > x1:
                for i in range(x2 - x1 + 1):
                    plane[y1][x1 + i] = str(int(plane[y1][x1 + i]) + 1) + " "
    return plane

def checkDiagnal(coordinants, plane):
    for coordinant in coordinants:
        x1 = int(coordinant[0][0])
        x2 = int(coordinant[1][0])
        y1 = int(coordinant[0][1])
        y2 = int(coordinant[1][1])
        if x1 == x2 or y1 == y2:
            continue    
        slope = (y1 - y2)/(x1 - x2)

        if slope == -1:
            if x1 > x2:
                for i in range(x1 - x2 + 1):
                    plane[y1 + i][x1 - i] = str(int(plane[y1 + i][x1 - i]) + 1) + " "

            if x2 > x1:
                for i in range(x2 - x1 + 1):
                    plane[y2 + i][x2 - i] = str(int(plane[y2 + i][x2 - i]) + 1) + " "    

        elif slope == 1:

            if x2 > x1:
                for i in range(x2 - x1 + 1):
                    plane[y1 + i][x1 + i] = str(int(plane[y1 + i][x1 + i]) + 1) + " "

            if x1 > x2:
                for i in range(x1 - x2 + 1):
                    plane[y2 + i][x2 + i] = str(int(plane[y2 + i][x2 + i]) + 1) + " "  

plane = checkHorizVert(coordinants, plane)
checkDiagnal(coordinants, plane)

print("                      ")
printPlane(plane)
count = 0
for y in plane:
    for x in y:
        if str(x) != "1 " and str(x) != "0 ":
            count += 1

print(count)
