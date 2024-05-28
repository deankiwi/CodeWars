
from pprint import pprint
from typing import List

from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        height, width = len(board), len(board[0])

        visited = set()

        def bfs(j, i) -> bool:
            captured = True
            stack = deque()
            stack.append((j, i))
            visited.add((j, i))
            temp_visit = set()
            temp_visit.add((j, i))

            while len(stack) > 0:
                row, col = stack.popleft()
                directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
                for j, i in directions:
                    row_2 = row + j
                    col_2 = col + i
                    place = board[row_2][col_2]
                    if place == "O":
                        if row_2 in [0, height - 1] or col_2 in [0, width - 1]:
                            captured = False
                        elif (row_2, col_2) not in temp_visit:
                            visited.add((row_2, col_2))
                            temp_visit.add((row_2, col_2))
                            stack.append((row_2, col_2))
            if captured:
                for j, i in temp_visit:
                    board[j][i] = "X"

            return captured

        for j in range(1, height - 1):
            for i in range(1, width - 1):
                if board[j][i] == "O" and (j, i) not in visited:
                    bfs(j,i)


board = [
    ["X", "O", "X", "X"],
    ["O", "X", "O", "X"],
    ["X", "O", "X", "O"],
    ["O", "X", "O", "X"],
]
pprint(board)
print()
Solution().solve(board)
pprint(board)

"""
130. Surrounded Regions
Medium
Topics
Companies
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

Example 1:


Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.
Example 2:

Input: board = [["X"]]
Output: [["X"]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
"""


'''
Faster solution was to only check the edge of the board first

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def dfs(x, y):
            board[x][y] = '#' # mark as protected
            for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0 <= x2 < m and 0 <= y2 < n and board[x2][y2] == 'O':
                    dfs(x2, y2)

        # dfs from 'O's on border
        for i in range(m):
            if board[i][0] == 'O': dfs(i, 0)
            if board[i][n-1] == 'O': dfs(i, n-1)
        for j in range(n):
            if board[0][j] == 'O': dfs(0, j)
            if board[m-1][j] == 'O': dfs(m-1, j)

        # flip surrounding regions
        for x in range(m):
            for y in range(n):
                if board[x][y] == 'O':
                    board[x][y] = 'X' # change to 'X'
                elif board[x][y] == '#':
                    board[x][y] = 'O' # change back to 'O'
'''

