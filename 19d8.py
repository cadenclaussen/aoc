import copy

with open("19d8.txt") as f:
    a = f.read().strip()

xDim = 25
yDim = 6
layerSize = xDim * yDim

board = []
for i in range(0, len(a), layerSize):
    board.append(a[i:i+layerSize])

#print(board)
zeroCounts = [layer.count("0") for layer in board]
#print(zeroCounts)
minZeros = min(zeroCounts)
#print(minZeros)
layerNumber = zeroCounts.index(minZeros)
#print(layerNumber)

answer = board[layerNumber].count("1") * board[layerNumber].count("2")
print("Part 1: " + str(answer))


#for j, layer in enumerate(board):
   # cur = []
   # for i in range(yDim):
       # cur.append(layer[i * xDim:(i+1) * xDim])

   # board[j] = cur.deepcopy()

#print(board)
picture = []
for i in range(layerSize):
    depth = 0
    while board[depth][i] not in "01":
        depth += 1
    picture.append(board[depth][i])

cur = []
for i in range(yDim):
    cur.append(picture[i * xDim:(i+1) * xDim])
print(cur)

for line in cur:
    print("".join(line).replace("0", " ").replace("1", "#"))

#picture = []
#for j, layer in enumerate(board):
   # for line in range(yDim)):
       # depth = 0
       # while board[depth][line] not in "01":
          #  depth += 1
  #      picture.append(board[depth][line])
