with open("21d25.txt") as f:
        lines = f.read().strip().split("\n")

def main():
        board = createBoard(lines)
        print("Initial board")
        printBoard(board)
        step(board)

def createBoard(lines):
        board = []
        for line in lines:
                characters = list(line)
                board.append(characters)
        return board

def step(board):
        step = 0
        moves = True
        #while moves:
        for i in range(4):
                board, movesEast = eastHerd(board)
                board, movesSouth = southHerd(board)
                moves = movesEast or movesSouth
                step += 1
                print()
                print(step)
                printBoard(board)
        return step

def eastHerd(board):
        moves = False
        skip = False
        for y in range(len(board)):
                for x in range(len(board[0])):

                        if skip:
                                skip = False
                                continue

                        if board[y][x] != ">":
                                continue

                        # > is at the end of the row, wrap
                        if x == len(board[0]) - 1:
                                if board[y][0] == ".":
                                        board[y][x] = "."
                                        board[y][0] = ">"
                                        moves = True
                                        # I don't think this skip is useful because after this we go to the next line
                                        # skip = True
                                continue

                        # > is NOT at the end of the row
                        if board[y][x + 1] == ".":
                                board[y][x] = "."
                                board[y][x + 1] = ">"
                                moves = True
                                skip = True

        return board, moves

def southHerd(board):
        moves = False
        skip = False
        for x in range(len(board[0])): # 0 1 2
                for y in range(len(board)):

                        if skip:
                                skip = False
                                continue

                        if board[y][x] != "v":
                                continue

                        if y == len(board) - 1:
                                if board[0][x] == ".":
                                        board[y][x] = "."
                                        board[0][x] = "v"
                                        moves = True
                                        # skip = True
                                continue

                        if board[y + 1][x] == ".":
                                board[y][x] = "."
                                board[y + 1][x] = "v"
                                moves = True
                                skip = True

        return board, moves

def printBoard(board):
        print(" ", end="")
        for _ in range(len(board[0])):
                print("_", end="")
        print()

        for string in board:
                print("|", end="")
                for y in range(len(string)):
                        print(string[y], end="")
                print()

main()
