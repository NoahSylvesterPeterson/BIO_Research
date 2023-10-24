# CS 143 Artificial Intelligence Assignment \#6
# author: (Noah Peterson)
# proposed points: 10 (out of 10)  -- not changing this line automatically results a 1 point deduction
#(4 points): implement the minimax algorithm, including implementing a simple utility function
# that will reward a “win” with a positive number and a loss with a negative number. All other
# configurations should return a 0.
#See Utility Test: 120-127,  Minmax: 207-225 
# (3 points): implement a depth parameter that will terminate the search a return the utility
# function.
#See Minmax: 207-225 
# (2 points): implement alpha-beta pruning. You should include in your submission evidence that
# your implementation is effective. For example, supply a description (or timings) that you are able
# to run your program with a deeper depth than you could without the alpha-beta pruning
# implementation.
#See Alpha_Beta: 242-293
# (1 points): implement a more sophisticated utility function that provides improved performance
# in your program.
#See utility: 129-143,   Points: 145-198

# comments: Special thanks to Keith Galli for supplying the foundation for the Connect 4 code
#           https://github.com/KeithGalli/Connect4-Python
import time
import math 
NUMBER_OF_ROWS = 6
NUMBER_OF_COLS = 7

HUMAN_PLAYER = 'x'
AI_PLAYER = 'o'

class ConnectFourGame :

    def __init__(self):
        # initialize the starting board
        self.initial = [['.'] * NUMBER_OF_COLS for _ in range(NUMBER_OF_ROWS)]

    def display(self, state):
        """Print or otherwise display the state."""
        print()
        for row in range(NUMBER_OF_ROWS-1,-1,-1):
            print("|\t",end='')
            for col in range(NUMBER_OF_COLS):
                print(state[row][col],"\t", end="")
            print("|")

        print("-" * 66)
        bk = "   |   "
        print(" "*8+"0"+bk+"1"+bk+"2"+bk+"3"+bk+"4"+bk+"5"+bk+"6") 


    def is_valid_location(self, state, col):
        if col <0 or col >= NUMBER_OF_COLS:
            return False
        else:
            return state[NUMBER_OF_ROWS - 1][col] == '.'

    def get_next_open_row(self, state, col):
        for r in range(NUMBER_OF_ROWS):
            if state[r][col] == '.':
                return r
        return NUMBER_OF_ROWS

    def winning_state(self, state, piece):
        # Check horizontal locations for win
        for c in range(NUMBER_OF_COLS - 3):
            for r in range(NUMBER_OF_ROWS):
                if state[r][c] == piece and state[r][c+1] == piece and state[r][c+2] == piece and state[r][c+3] == piece:
                    return True

        # Check vertical locations for win
        for c in range(NUMBER_OF_COLS):
            for r in range(NUMBER_OF_ROWS - 3):
                if state[r][c] == piece and state[r+1][c] == piece and state[r+2][c] == piece and state[r+3][c] == piece:
                    return True

        # Check positively sloped diaganols
        for c in range(NUMBER_OF_COLS - 3):
            for r in range(NUMBER_OF_ROWS - 3):
                if state[r][c] == piece and state[r+1][c+1] == piece and state[r+2][c+2] == piece and state[r+3][c+3] == piece:
                    return True

        # Check negatively sloped diaganols
        for c in range(NUMBER_OF_COLS - 3):
            for r in range(3, NUMBER_OF_ROWS):
                if state[r][c] == piece and state[r-1][c+1] == piece and state[r-2][c+2] == piece and state[r-3][c+3] == piece:
                    return True
        return False

    def terminal_test(self, state):
        return self.winning_state(state, "x") or self.winning_state(state, "o") or len(self.actions(state)) == 0


    def actions(self, state):
        # returns list of numbers corresponding to possible moves
        valid_locations = []
        for col in range(NUMBER_OF_COLS):
            if self.is_valid_location(state, col):
                valid_locations.append(col)
        return valid_locations

    def result(self, state, move, player):
        """Return the state that results from making a move from a state."""
        row = self.get_next_open_row(state, move)
        state[row][move] = player
        return state

    def undo(self, state, move):
        """Undo a given move. return the state"""
        row = self.get_next_open_row(state, move)
        state[row-1][move] = '.'
        return state

    def getEnemyPlayer(self,player):
        # return the opposite of player
        if player == 'x':
            return 'o'
        else:
            return 'x'


    def utilityTest(self, state, piece):
        if self.winning_state(state, piece):
            return 1000
        elif self.winning_state(state, self.getEnemyPlayer(piece)):
            return -1000
        else:
            return 0 

    
    def utility(self, state, piece):
        """Return the value of this state for the player."""
        # cheack to see if this is a winning state, if so pick it.
        if self.winning_state(state, 'o'):
            return 1000
        # check to see if this allows your apponent to win in which case dont pick it. 
        else:
            for i in range(7):
                if self.is_valid_location(state, i):
                    if self.winning_state(self.result(state, i, 'x'), 'x'):
                        self.undo(state,i)
                        return(-1000)
                    else:
                        self.undo(state,i)
        return(self.Points(state, 'o')- self.Points(state, 'x'))
        
    def Points(self, state, piece):
        """Returns the number of points a player has,
gives so many points for an unblocked 3 in a row and unblocked 2 in a row"""
        # Check horizontal locations for points
        # for three in a row 
        thr = 27 
        #for 2 in a row
        tw = 8
        #start tally for points
        count = 0
        # Check horizontal locations for points
        for c in range(NUMBER_OF_COLS - 3):
            for r in range(NUMBER_OF_ROWS):
                #checks each row for how many of the correct pieces are in a row if the apponent has a piece that can block this, award not points
                m = (state[r][c] == piece) + ( state[r][c+ 1] == piece) + ( state[r][c+ 2] == piece) + ( state[r][c+ 3] == piece)- (10)*((state[r][c] == self.getEnemyPlayer(piece)) or ( state[r][c+ 1] == self.getEnemyPlayer(piece)) or ( state[r][c+ 2] == self.getEnemyPlayer(piece)) or ( state[r][c+ 3] == self.getEnemyPlayer(piece)))
                #if we have 3 in a row unblocked then award thr points 
                if  m == 3:
                    count = count +   thr
                #if we have 2 in a row unblocked then award tw points 
                elif m == 2:
                    count = count +   tw
        # Check vertical locations for points
        for c in range(NUMBER_OF_COLS):
            for r in range(NUMBER_OF_ROWS - 3):
                m = (state[r][c] == piece) + ( state[r+ 1][c] == piece) + ( state[r+ 2][c] == piece) + ( state[r+ 3][c] == piece)- (10)*((state[r][c] == self.getEnemyPlayer(piece)) or ( state[r+ 1][c] == self.getEnemyPlayer(piece)) or ( state[r+ 2][c] == self.getEnemyPlayer(piece)) or ( state[r+ 3][c] == self.getEnemyPlayer(piece)))
                if m == 3:
                    count = count +   thr
                elif m == 2:
                    count = count +   tw

        # Check positively sloped diaganols
        for c in range(NUMBER_OF_COLS-3):
            for r in range(NUMBER_OF_ROWS - 3):
                m = (state[r][c] == piece) + ( state[r+ 1][c+ 1] == piece) + ( state[r+ 2][c+ 2] == piece) + ( state[r+ 3][c+ 3] == piece)- (10)*((state[r][c] == self.getEnemyPlayer(piece)) or ( state[r+ 1][c+ 1] == self.getEnemyPlayer(piece)) or ( state[r+ 2][c+ 2] == self.getEnemyPlayer(piece)) or ( state[r+ 3][c+ 3] == self.getEnemyPlayer(piece)))
                if m == 3:
                    count = count +   thr
                elif m == 2:
                    count = count +   tw

        # Check negatively sloped diaganols
        for c in range(NUMBER_OF_COLS-3):
            for r in range(3,NUMBER_OF_ROWS):
                m = (state[r][c] == piece) + ( state[r-1][c+ 1] == piece) + ( state[r-2][c+ 1] == piece) + ( state[r-3][c+ 3] == piece) - (10)*((state[r][c] == self.getEnemyPlayer(piece)) or ( state[r-1][c+ 1] == self.getEnemyPlayer(piece)) or ( state[r- 2][c+ 2] == self.getEnemyPlayer(piece)) or ( state[r- 3][c+ 3] == self.getEnemyPlayer(piece)))
                if m == 3:
                    count = count +   thr
                elif m == 2:
                    count = count +  tw
            
        #give some points for controlling the middle 
        for c in range(NUMBER_OF_COLS):
            for r in range(NUMBER_OF_ROWS - 3):
                if state[r][c] == piece:
                    count = count + 3 - abs(c-3)
        return count

    
    
    
    
    
    
    
    def minimax(self,  state, depth, player) :
        #most of this was copied from the tick tack toe 
        bestMove = 0 
        if depth == 0 or self.terminal_test(state):
#################################################################################################
            #Toggle Between utilities: utilityTest is the only win or loss utility 
            #return self.utilityTest(state, 'o'), None
            return self.utility(state, 'o'), None
#################################################################################################
        if player == "o": #maximizing player
            best = -math.inf
            
            for move in self.actions(state):
                state = self.result(state, move, player)
                val, _ = self.minimax(state,depth-1, self.getEnemyPlayer(player))
                self.undo(state,move)
                
                if val >= best :
                    best, bestMove = val, move

        else: #minimizing player

                    
            best = math.inf
            
            for move in self.actions(state):
                state = self.result(state, move, player)
                val, _ = self.minimax(state, depth-1, self.getEnemyPlayer(player))
                self.undo(state,move)

                if val <= best :
                    best, bestMove = val, move
        return best, bestMove
    
    
    def Alpha_Beta(self,  state, depth, player, a, b) :
        #most of this was copied from min max
        bestMove = 0 
        if depth == 0 or self.terminal_test(state):
#################################################################################################
            #Toggle Between utilities: utilityTest is the only win or loss utility 
            #return self.utilityTest(state, 'o'), None
            return self.utility(state, 'o'), None
#################################################################################################

        if player == "o": #maximizing player
            best = -math.inf
            
            for move in self.actions(state):
            
                state = self.result(state, move, player)
                val, _ = self.Alpha_Beta(state,depth-1, 'x',a,b)
                self.undo(state,move)
                
                
                if val >= best:
                    best, bestMove = val, move 
                
                if val > a:
                    a = val
                    
                if a >= b :
                    break
                
                
                
                   

        else: #minimizing player

                    
            best = math.inf
            
            for move in self.actions(state):
                state = self.result(state, move, player)
                val, _ = self.Alpha_Beta(state, depth-1, 'o',a,b)
                self.undo(state,move)
                
                if val <= best:
                    best, bestMove = val, move 
                
                if val < b:
                    b = val
                
                if a > b :
                    break
        return best, bestMove
    
    def play(self, state):
        """" play a game of connect 4 """
        game_over = False
        turn = 1
        while not game_over:
            self.display(state)
            if turn == 1:
                print("PLAYER 1")
                col = int(input("Where to drop a piece?"))
                if self.is_valid_location(state, col):
                    state = self.result(state, col, 'x')
                    turn = 2
                else:
                    print('not a valid location; try again')

                if self.winning_state(state, 'x'):
                    print("Player 1 wins!")
                    game_over = True

            else:
                print("PLAYER 2")
                startTime = time.time()
####################################################################################################################
                #Toggle between Minmax and Alpha_Beta
                val, col = self.Alpha_Beta(state, 4,'o',-math.inf, math.inf)
                #val, col = self.minimax(state, 4,'o')
#####################################################################################################################
                if self.is_valid_location(state, col):
                    state = self.result(state, col, 'o')

                    turn = 1
                else:
                    print(str(col) +' is not a vaild location; try again')

                if self.winning_state(state, 'o'):
                    print("Player 2 wins!")
                    game_over = True
                print("Time taken: " + str(time.time()-startTime))
        self.display(state)

#play the game
game = ConnectFourGame()
game.play(game.initial)