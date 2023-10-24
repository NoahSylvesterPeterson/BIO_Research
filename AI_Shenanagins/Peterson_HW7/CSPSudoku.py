from CSP import *

import math
import random

class CSPSudoku(CSP):

    def __init__ (self, variables, domains):
        # a list of variables
        # a dictionary of domains: a mapping of variables to a list of possible values
        super().__init__(variables,domains)


    def printBoard(self):
        for row in range(9):
            for col in range(9):
                val = "n"
                num = len(self.domains[self.variables[row * 9 + col]])
                if num == 1:
                    val = str(self.domains[self.variables[row * 9 + col]][0])
                elif num > 1:
                    val = "."
                print(val, end="")

                if (col == 2 or col == 5):
                    print ("|", end = "")
            print()

            if (row == 2 or row == 5):
                for col in range(11):
                    print("-", end="")
                print()


    def chooseVariable(self, assignment):
        minVals = math.inf
        minList = []
        for variable in self.variables:
            if variable not in assignment:
                numVals = len(self.domains[variable])
                if numVals < minVals:
                    minVals = numVals
                    minList = [variable]
                elif numVals == minVals:
                    minList.append(variable)

        if len(minList) > 1:
            # break ties by constraints
            maxCons = 0
            maxList = []
            for variable in minList:
                numCons = len(self.constraints[variable])
                if numCons > maxCons:
                    maxCons = numCons
                    maxList = [variable]
                elif numCons == maxCons:
                    maxList.append(variable)

            if len(maxList) > 1:
                return random.choice(maxList)
            else:
                return maxList[0]

        else:
            return minList[0]
