from CSPSudoku import *
import time

letters = "ABCDEFGHI"

def readFromFile(filename):
    board = ""
    file = open(filename, "r")
    lines = file.readlines()
    for line in lines:
        board =line.replace("\n", "")
    return board

def addRowConstraints(row, col, csp):
    var1 = letters[row] + str(col + 1)
    for c in range(col + 1, 9):
        var2 = letters[row] + str(c + 1)
        csp.addConstraint(var1, var2)

def addColConstraints(row, col, csp):
    var1 = letters[row] + str(col + 1)
    for r in range(row + 1, 9):
        var2 = letters[r] + str(col + 1)
        csp.addConstraint(var1, var2)

def addSquareConstraints(row, col, csp):
    var1 = letters[row] + str(col + 1)

    squareRow = row // 3
    squareCol = col // 3

    for r in range(3):
        for c in range(3):
            newRow = squareRow * 3 + r
            newCol = squareCol * 3 + c

            if newRow != row and newCol != col:
                var2 = letters[newRow] + str(newCol + 1)
                csp.addConstraint(var1, var2)



def main():
    board =readFromFile("sudokuTestHard.txt")

    variables = []
    domains = {}

    for row in letters:
        for col in range(1,10):
            variables.append(row+str(col))

    for row in range(9):
        for col in range(9):
            index = row * 9 + col
            value = board[index]
            if value == ".":
                values = [i for i in range(1, 10)]
            else:
                values = [int(value)]

            domains[letters[row] + str(col + 1)] = values

    myCSP = CSPSudoku(variables, domains)

    # add the constraints
    for row in range(9):
        for col in range(9):
            addRowConstraints(row, col, myCSP)
            addColConstraints(row, col, myCSP)
            addSquareConstraints(row, col, myCSP)

    print("***********")


    myCSP.printBoard()
    starttime = time.time()
    myCSP.ac3()

    if not myCSP.solved():
        print("\nnot able to be solved with AC3 alone.... using backtracking...\n")
        myCSP.search()

    stoptime = time.time()
    totaltime = stoptime - starttime
    print("total time:", totaltime)
    print("@@@@@@@@@@@")
    myCSP.printBoard()
main()