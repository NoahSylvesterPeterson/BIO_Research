# This entire file will need to be changed. 





from EightPuzzle import *
from UniformCostSearch import *
from AStarSearch import *
# create the problem model
# eight_puzzle = SlidingPuzzle(3,3,(1, 2, 3, 4, 5, 6, 0, 7, 8))  # requires 2 moves

# other examples of creating an 8-puzzle problem
#eight_puzzle = SlidingPuzzle(3,3,(1, 2, 3, 4, 5, 7, 8, 6, 0)) #requires 12 moves
#eight_puzzle = SlidingPuzzle(3,3,(2, 3, 1, 8, 0, 6, 5, 7, 4)) # requires 24 moves

eight_puzzle = SlidingPuzzle(5,5,(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)) #start with solution
eight_puzzle.shuffle(200) # make moves to ensure the puzzle is in a solvable state, but mixed up a bit


# search using Uniform Search
myUCSearch = UniformCostSearch(eight_puzzle)
result_node = myUCSearch.search()

if (result_node is None):
    print("No path found using Uniform Cost search!")
else:
    print("Path:", result_node.path())
    print("Path Cost:", result_node.path_cost)
    print("Solution:", result_node.solution())
print("Nodes searched with UCS search:", myUCSearch.nodesSearched)
print("Time Spent with  UCS search:", myUCSearch.timeSpent)


print("==============")

# search using A Star Search
myAStarSearch = AStarSearch(eight_puzzle)
result_node = myAStarSearch.search()

if (result_node is None):
    print("No path found using A Star search!")
else:
    print("Path:", result_node.path())
    print("Path Cost:", result_node.path_cost)
    print("Solution:", result_node.solution())
print("Nodes searched with A Star search:", myAStarSearch.nodesSearched)
print("Time Spent with A Star search:", myAStarSearch.timeSpent)


print("==============")