from time import time
'''
This program solves for the minimal number of moves for a Knight to move to a specified position on a chess board

We are given a board size N-by-N, a Knight starting at position_start, and a goal position of position_goal (Both specified positions are within the board's boundaries)

Setup:
    We create an object/struct – cell - to hold values x, y, and distance
    We create a utility function to determine whether a given position is within the Chess board boundaries

Approach:
    Check if the goal position is within the Chess board boundaries - immediately return -1 if it is not
    Create a list to act as a queue (Just FIFO)
    Create two lists to show the possible moves that a Knight can move (8 possible moves: 2 right 1 down, 2 right 1 up, etc.)
    Create a matrix of size N-by-N using a 2D list – initialize all values to 0

    We start with the initial position position_initial, and add it as a cell to the queue
    Now we loop:
        Pop from the front of queue list
        If the current cell is at the goal position:
            return the cell's distance --> Program ends here
        Else:
            now we loop again!:
                For each possible move from our moves lists, we add to our current position and we check if the new position has been visited in our matrix
                If it was:
                    continue and iterate to the next values
                Else:
                    add this new position as a cell to the queue, with the old cell's distance + 1 (This is one more move, and thus one distance further from our starting point)
    

'''

# Simple Cell struct -- contains a position's x-value, y-value, and its distance from the starting point (moves since starting point, not literal displacement)
class Cell: 
    def __init__(self, x:int=0, y:int=0, dist:int=0):
        self.x = x
        self.y = y
        self.distance = dist

# Simple utility function that returns True if the specified x and y values are within the board's N-by-N grid
def isValid(x:int, y:int, N:int) -> bool:
    if x<0 or y<0 or x>=N or y>=N:
        return False
    return True


def minKnightMoves(N:int, startX, startY, goalX, goalY ) -> int:
    if not isValid(goalX,goalY,N):
        return -1
    
    matrix = [[0 for i in range(N)] for j in range(N)]          # Visited positions matrix
    queue = []                                                  # Queue of cells
    start = Cell(startX,startY, 0)    # Starting position cell
    
    queue.append(start)
    matrix[startX][startY] = 1                                # Mark initial position as visited

    moves = [[2, 2, -2, -2, 1, 1, -1, -1],       # Possible directions in x-plane
             [1, -1, 1, -1, 2, -2, 2, -2]]      # Possible directions in y-plane
    
    # loop while the queue has cells – will have an absolute end once all possible moves have been completed
    while queue:
        pos = queue.pop(0) # retrieve from front of queue (least recent cell)

        # Functional base case
        if pos.x == goalX and pos.y == goalY:
            return pos.distance                                 # exits here eventually if goal is reachable

        # iterate through each possible move and check if they are possible
        for m in range(8):  
            dx = moves[0][m]
            dy = moves[1][m]
            # add current move to the position and save as newX and newY – hence the names
            newX = pos.x + dx
            newY = pos.y + dy   

            # if the new position is valid and has not been visited before
            if isValid(newX, newY, N) and matrix[newX][newY] == 0:
                # Create new cell (with incremented distance) and append it to the queue
                newPos = Cell(newX, newY, pos.distance + 1)
                queue.append(newPos)
                # Mark the new position as now visited
                matrix[newX][newY]+=1


# Edit inputs here
N = 9
pi = position_initial = [0,0]
pg = position_goal = [7,6]
t1 = time()
moves = minKnightMoves(N, pi[0], pi[1], pg[0], pg[1])
t2 = time() 
print
print("Moves: \t " + str(moves))
print("Runtime: " + str(t2-t1))
            





