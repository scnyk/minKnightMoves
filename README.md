# minKnightMoves

In the game of chess, any given knight has eight possible moves.

![image](https://github.com/scnyk/minKnightMoves/assets/131561465/776cd60e-a3f5-4731-872f-e9176d6365a6)


Given an N-by-N chess board, a starting position, and a goal position, how can we find the optimal (Minimal) number of moves for the knight to reach the given goal?

# Approach: 

This strategy follows a method that follows [Djikstra's Algorithm](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/) using BFS. The program starts at the root vertex and checks all adjacent vertices, repeating and recording the number of edges traversed until the goal vertex is found.

First we define a Cell class/struct with properties x, y, and distance – this will record a given position and its 'distance' from the starting position (vertex).

We then create 4 things to start the main function:
- An empty queue
- A Cell for the starting position with a distance of 0 (since it is the starting vertex)
- A list containing the possible moves (two lists for the different axes)
- A matrix to record the visited Cells, initialized to None or 0
We add the starter Cell to the queue and set the corresponding matrix Cell to 1


Now we start looping while the queue is not empty:

Pop the first Cell from the queue and check if the position is the goal position; if it is, return the Cell's distance.

Otherwise, iterate for each possible move in the moves list:
- Create a new Cell, adding the current move to the original Cell's position, with the original distance + 1
- If the new Cell was already visited in the visits matrix, continue to the next matrix, otherwise add the new Cell to the end of the queue then continue

