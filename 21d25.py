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
        if moves:
            step += 1
            print()
            print("After " + str(step) + " step(s):")
            printFloor(floor)
    return step

def eastHerd(floor):
    moves = False
    for y in range(len(floor)):
        x = 0
        while x < len(floor[0]):
            if floor[y][x] == ">":
                if x == len(floor[0]) - 1:
                    if (floor[y][0] == "."):
                        # > is at the end of the row, '.' at beg, wrap the move
                        moves = True
                        floor[y][x] = "."
                        floor[y][0] = ">"
                elif floor[y][x + 1] == ".":
                    # > is NOT at the end of the row
                    moves = True
                    floor[y][x] = "."
                    floor[y][x + 1] = ">"
                    # Skip the next x since it is our just moved ">"
                    x += 1
            x += 1
    return floor, moves

def southHerd(floor):
    moves = False
    for x in range(len(floor[0])):
        y = 0
        while y < len(floor):
            if floor[y][x] == "v":
                if y == len(floor) - 1:
                    if floor[0][x] == ".":
                        moves = True
                        floor[y][x] = "."
                        floor[0][x] = "v"
                elif floor[y + 1][x] == ".":
                    moves = True
                    floor[y][x] = "."
                    floor[y + 1][x] = "v"
                    y += 1
            y += 1
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
