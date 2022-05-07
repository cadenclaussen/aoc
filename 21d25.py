with open("21d25.txt") as f:
    lines = f.read().strip().split("\n")

def main():
    floor = createFloor(lines)
    print("Initial state:")
    printFloor(floor)
    step(floor)

def createFloor(lines):
    floor = []
    for line in lines:
        characters = list(line)
        floor.append(characters)
    return floor

def step(floor):
    step = 0
    moves = True
    while moves:
        floor, movesEast = eastHerd(floor)
        floor, movesSouth = southHerd(floor)
        moves = movesEast or movesSouth
        step += 1
        print()
        print("After " + str(step) + " step(s):")
        printFloor(floor)
    return step

def eastHerd(floor):
    moves = False
    changes = []
    for y in range(len(floor)):
        for x in range(len(floor[0])):
            if floor[y][x] == ">":
                if x == len(floor[0]) - 1:
                    if (floor[y][0] == "."):
                        # > is at the end of the row, '.' at beg, wrap the move
                        changes.append([[y, x], [y, 0]])

                elif floor[y][x + 1] == ".":
                    # > is NOT at the end of the row
                    changes.append([[y, x], [y, x+1]])

    for change in changes:
        floor[change[0][0]][change[0][1]] = "."
        floor[change[1][0]][change[1][1]] = ">"
        moves = True

    return floor, moves

def southHerd(floor):
    moves = False
    changes = []
    for x in range(len(floor[0])):
        for y in range(len(floor)):
            if floor[y][x] == "v":
                if y == len(floor) - 1:
                    if floor[0][x] == ".":
                        changes.append([[y, x], [0, x]])

                elif floor[y + 1][x] == ".":
                    changes.append([[y, x], [y+1, x]])

    for change in changes:
        floor[change[0][0]][change[0][1]] = "."
        floor[change[1][0]][change[1][1]] = "v"
        moves = True

    return floor, moves

def printFloor(floor):
    print(" ", end="")
    for _ in range(len(floor[0])):
        print("_", end="")
    print()

    for row in floor:
        print("|", end="")
        for y in range(len(row)):
            print(row[y], end="")

        print()

main()
