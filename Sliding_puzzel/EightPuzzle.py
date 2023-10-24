
from Problem import *
from math import *
from LZCompression import *
from random import randrange 

def makeBinary(n,l):
    """returns a string representing an integer in binary"""
    rem = n
    oupt = ""
    for i in range(l):
        #print(2**(l-i-1))
        if rem >= 2**(l-i-1):
            oupt += "1"
            rem -= 2**(l-i-1)
        else:
            oupt += "0"
    return(oupt)

def StateToBinary(state,l):
    """converts state to binary string"""
    oupt = ""
    for i in state:
        oupt += makeBinary(i,l)
    return oupt


class SlidingPuzzle(Problem):
    """ The problem of sliding tiles numbered from 1 to 8 on a 3x3 board,
    where one of the squares is a blank. A state is represented as a tuple of length 9,
    where element at index i represents the tile number  at index i (0 if it's an empty square) """

    def __init__(self, x, y, initial, blanks = 1 ):
        """ Define goal state and initialize a problem """
        n = x*y - blanks
        self.n = n
        self.BinaryLength = int(floor(log(n,2)) + 1)
        goal = []
        for i in range(blanks):
            goal.append(0)
        for i in range(n):
            goal.append(i+1)
        self.goal = tuple(goal)
        binaryGoal = ""
        for i in range(blanks):
            binaryGoal += "0"*self.BinaryLength
        for i in range(n):
            binaryGoal += makeBinary(i+1,self.BinaryLength)

        self.BinaryGoal = binaryGoal
        self.x = x
        self.y = y
        self.blanks = blanks 
        #self.map = {1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),0:(2,2)}
        Problem.__init__(self, initial, goal)

    def find_blank_square(self, state):
        """Return the index of the blank square in a given state"""
        zeros = []
        for i in range(len(state)):
            if state[i] == 0:
                zeros.append(i)
        return zeros

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """

        possible_actions = []
        index_blanks= self.find_blank_square(state)
        for index_blank_square in index_blanks:
            if index_blank_square % self.x != 0:
                possible_actions.append((index_blank_square ,'LEFT'))
            if index_blank_square >= self.x:
                possible_actions.append((index_blank_square ,'UP'))
            if index_blank_square % self.x != self.x-1:
                possible_actions.append((index_blank_square ,'RIGHT'))
            if index_blank_square <= (self.y-1)*self.x -1:
                possible_actions.append((index_blank_square ,'DOWN'))

        return possible_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        # blank is the index of the blank square
        blank = action[0]
        action = action[1]
        new_state = list(state)

        delta = {'UP': -self.x, 'DOWN': self.x, 'LEFT': -1, 'RIGHT': 1}
        neighbor = blank + delta[action]
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]

        return tuple(new_state)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """
        for i in range(len(state)):
            if state[i] != self.goal[i]:
                return(False)
        else:
            return True

    def shuffle(self, number_of_moves):
        """ shuffle the initial state by number_of_moves"""
        import random
        state = self.initial
        for i in range(number_of_moves):
            possible_actions = self.actions(state)
            act = random.choice(possible_actions)
            state = self.result(state,act) #make a random move
        self.initial = state


    #def h(self, state):
    #    """ hueristic cost # of out of place squares"""
    #    #ToDo: Implement this function to return a hueristic cost for the state
    #    count = 0
    #    for i in range(len(state)):
    #        if state[i] != self.goal[i]:
    #            count = count + 1
    #    return count

    def h(self, state):
        return(randrange(0,100))
    
    def h1(self, state):
        BinaryState = StateToBinary(state, self.BinaryLength)
        #compression = Mutual_Compression_ratio(self.BinaryGoal,BinaryState) #worse than uniform 135957
        compression = 1-Mutual_Compression_Crossed(self.BinaryGoal,BinaryState) # worse than uniform 147376
        return((compression)*100)






#    def h1(self, state):
#        """ hueristic cost min """
#        #ToDo: Implement this function to return a hueristic cost for the state
#        count = 0
#        for i in range(len(state)):
#            n = state[i]
#            if n != 0:
#                n = self.map[n]
#                count = count + abs(floor(i/3)-n[0]) + abs(i%3 - n[1])
#        return count 

