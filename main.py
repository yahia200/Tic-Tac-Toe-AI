import numpy as np


def most_frequent(lis):
    return max(set(lis), key=lis.count)


def printBoard(boar):
    l=[]
    for i in boar:
        for n in i:
            if n == 3:
                l += [" X "]
            if n == 5:
                l += [" O "]
            if n == 0:
                l += [" * "]

    for n in range(0, 9):
        if n in [2, 5]:
            print(l[n])
        else:
            print(l[n], end="")
    print("")



#start of setup
print("Grid:")
for i in range(0,7,3):
    print(f"{i}  {i+1}  {i+2}")
X = 3
O = 5
board = np.ndarray((3, 3))
board.fill(0)
a = board.sum(1).tolist()
b = board.sum(0).tolist()
c = (board.diagonal()).sum()
d = np.fliplr(board).diagonal().sum()
prio = []
#end of setup

print("Enter cell number or [yf] to let the ai go first")
while 9 not in a and 15 not in a and 9 not in b and 15 not in b and d not in [9, 15] and c not in [9, 15]:
    n = input("Your move:  ")
    if n != "yf":
        board.put(n, O)
        if np.count_nonzero(board) == 9:
            break
    a = board.sum(1).tolist()
    b = board.sum(0).tolist()
    c = (board.diagonal()).sum()
    d = np.fliplr(board).diagonal().sum()
    if 15 not in a and 15 not in b and c != 15 and d != 15:
        # start of early game strat
        if n == "4":
            for i in [0, 2, 6, 8]:
                if board.item(i) == 0:
                    board.put(i, X)
                    printBoard(board)
                    break
            continue
        # end of early game strat

        if board.item(4) == 0:
            board.put(4, X)
            printBoard(board)
            continue

        # start of wining condition
        if 6 in a:
            row = 3 * a.index(6)
            for rx in range(row, row + 3):
                if board.item(rx) == 0:
                    board.put(rx, X)
                    printBoard(board)
                    break
            break

        if 6 in b:
            col = 3 * b.index(6)
            for hx in range(col, col + 7, 3):
                if board.item(hx) == 0:
                    board.put(hx, X)
                    printBoard(board)
                    break
            break

        if c == 6:
            for d1 in [0, 4, 8]:
                if board.item(d1) == 0:
                    board.put(d1, X)
                    printBoard(board)
                    break
            break

        if d == 6:
            for d2 in [2, 4, 6]:
                if board.item(d2) == 0:
                    board.put(d2, X)
                    printBoard(board)
                    break
            break
        # end of wining condition

        # start of losing condition
        if 10 in a:
            row = 3 * a.index(10)
            for ro in range(row, row + 3):
                if board.item(ro) == 0:
                    board.put(ro, X)
                    printBoard(board)
                    break
            continue

        if 10 in b:
            col = b.index(10)
            for ho in range(col, col + 7, 3):
                if board.item(ho) == 0:
                    board.put(ho, X)
                    printBoard(board)
                    break
            continue

        if c == 10:
            for d1 in [0, 4, 8]:
                if board.item(d1) == 0:
                    board.put(d1, X)
                    printBoard(board)
                    break
            continue

        if d == 10:
            for d2 in [2, 4, 6]:
                if board.item(d2) == 0:
                    board.put(d2, X)
                    printBoard(board)
                    break
            continue

        # end of losing condition
        # start of mid strat
        if c == 3:
            for d1 in [0, 4, 8]:
                if board.item(d1) == 0:
                    prio += 2 * [d1]

        if d == 3:
            for d2 in [2, 4, 6]:
                if board.item(d2) == 0:
                    prio += 2 * [d2]

        if 3 in a:
            rowx = 3 * (a.index(3))
            for bx in range(rowx, rowx + 3):
                if board.item(bx) == 0:
                    prio += [bx]

        if 3 in b:
            col = b.index(3)
            for hx in range(col, col + 7, 3):
                if board.item(hx) == 0:
                    prio += [hx]

        if len(prio) > 0:
            move = most_frequent(prio)
            board.put(move, X)
            printBoard(board)
            continue

        # end of mid strat

        a = board.sum(1).tolist()
        b = board.sum(0).tolist()
        c = (board.diagonal()).sum()
        d = np.fliplr(board).diagonal().sum()
        break


#start of last check
a = board.sum(1).tolist()
b = board.sum(0).tolist()
c = (board.diagonal()).sum()
d = np.fliplr(board).diagonal().sum()
#end of last check


print("")
if 9 in a or 9 in b or c == 9 or d == 9:
    print("X wins")
elif 15 in a or 15 in b or c == 15 or d == 15:
    print("O wins")
else: print("it is a draw!")
