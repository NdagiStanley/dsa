"""

This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board.
Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps
required to reach the end coordinate from the start. If there is no possible path, then return null.
You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the
edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required
to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere
else on the second row.
"""

# Ref: https://www.geeksforgeeks.org/shortest-distance-two-cells-matrix-grid/

# Python code to find number of unique paths in a
# matrix with obstacles.


def uniquePathsWithObstacles(A):

    # create a 2D-matrix and initializing with value 0
    paths = [[0] * len(A[0]) for i in A]
    # print(paths)

    # initializing the left corner if no obstacle there
    if A[0][0] == 0:
        paths[0][0] = 1

    # initializing first column of the 2D matrix
    for i in range(1, len(A)):
        if A[i][0] == 0:
            # If not obstacle
            paths[i][0] = paths[i - 1][0]

    # initializing first row of the 2D matrix
    for j in range(1, len(A[0])):
        if A[0][j] == 0:
            # If not obstacle
            paths[0][j] = paths[0][j-1]

    for i in range(1, len(A)):
        for j in range(1, len(A[0])):

            # If current cell is not obstacle
            if A[i][j] == 0:
                paths[i][j] = paths[i - 1][j] + paths[i][j - 1]

    # returning the corner value of the matrix
    return paths[-1][-1]


# Driver Code
A = [[0, 0, 0],
     [0, 1, 0],
     [0, 0, 0]]
print(uniquePathsWithObstacles(A))

# B = [[f, f, f, f],
#      [t, t, f, t],
#      [f, f, f, f],
#      [f, f, f, f]]
B = [[0, 0, 0, 0],
     [1, 0, 1, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]
print(uniquePathsWithObstacles(B))
