

from collections import defaultdict
from pprint import pprint
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check across
        for row in board:
            seen = defaultdict(int)
            for cell in row:
                if cell != "." and seen[cell]:

                    return False
                else:
                    seen[cell] += 1
        for column in range(len(board[0])):

            seen = defaultdict(int)
            for row in range(len(board)):
                cell = board[row][column]
                if cell != "." and seen[cell]:

                    return False
                else:
                    seen[cell] += 1
        for box_down in range(0, 9, 3):
            for box_across in range(0, 9, 3):
                seen = defaultdict(int)
                for down in range(3):
                    for across in range(3):

                        cell = board[box_down + down][box_across + across]
                        if cell != "." and seen[cell]:
                            return False
                        else:
                            seen[cell] += 1

        return True


# print(
#     Solution().isValidSudoku(
#         [
#             ["5", "3", ".", ".", "7", ".", ".", ".", "."],
#             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#             [".", "9", "8", ".", ".", ".", ".", "6", "."],
#             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#             [".", "6", ".", ".", ".", ".", "2", "8", "."],
#             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#             [".", ".", ".", ".", "8", ".", ".", "7", "9"],
#         ]
#     ),
#     "= True",
# )
# print(
#     Solution().isValidSudoku(
#         [
#             ["5", "3", ".", ".", "7", ".", ".", "5", "."],
#             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#             [".", "9", "8", ".", ".", ".", ".", "6", "."],
#             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#             [".", "6", ".", ".", ".", ".", "2", "8", "."],
#             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#             [".", ".", ".", ".", "8", ".", ".", "7", "9"],
#         ]
#     ),
#     "= False (horizontal)",
# )
# print(
#     Solution().isValidSudoku(
#         [
#             [".", ".", ".", ".", ".", ".", ".", ".", "."],
#             [".", ".", ".", ".", ".", ".", ".", ".", "."],
#             [".", ".", ".", ".", ".", ".", ".", ".", "."],
#             [".", ".", ".", ".", ".", ".", ".", ".", "."],
#             [".", "1", ".", ".", ".", ".", ".", ".", ""],
#             [".", ".", ".", ".", ".", ".", ".", ".", "."],
#             [".", ".", ".", ".", ".", ".", ".", ".", "."],
#             [".", ".", ".", ".", ".", ".", ".", ".", "."],
#             [".", ".", ".", ".", ".", ".", ".", ".", "."],
#         ]
#     ),
#     "= False (horizontal)",
# )


# print(
#     Solution().isValidSudoku(
#         [
#             [".", ".", ".", ".", ".", ".", ".", ".", "."],
#             [".", ".", ".", ".", ".", ".", ".", ".", "."],
#             [".", ".", ".", ".", ".", "1", ".", ".", "."],
#             [".", ".", ".", ".", ".", ".", ".", ".", "."],
#             [".", ".", ".", ".", ".", ".", ".", ".", "."],
#             [".", ".", ".", ".", ".", ".", ".", ".", "."],
#             [".", ".", ".", ".", ".", ".", ".", ".", "."],
#             [".", ".", ".", ".", ".", ".", ".", ".", "."],
#             [".", ".", ".", ".", ".", "1", ".", ".", "."],
#         ]
#     ),
#     "= False (vertically)",
# )
print(
    Solution().isValidSudoku(
        [
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "1", "."],
            [".", ".", ".", ".", ".", ".", "1", ".", "."],
        ]
    ),
    "= False (in box)",
)

"""
36. Valid Sudoku
Medium
Topics
Companies
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""


'''
other solutions that can do it in a single pass

def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        for i, row in enumerate(board):
            for j, x in enumerate(row):
                if x != '.':
                    res += [(i, x), (x, j), (i // 3, j // 3, x)]
        return len(res) == len(set(res))


or this one

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boardMap = collections.defaultdict(list)
        for x in range(9):
            for y in range(9):
                char = board[x][y]
                if char != '.': 
                    if char in boardMap:
                        for pos in boardMap[char]:
                            if (pos[0]== x) or (pos[1] == y) or (pos[0]//3 == x//3 and pos[1]//3 == y//3):
                                return False
                    boardMap[char].append((x,y))
   
        return True
'''

