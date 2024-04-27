
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i = 0
        j = 0
        output = []
        width = len(matrix[0])
        height = len(matrix)
        direction = "right" if width > 1 else "down"

        time_around = 0

        turns = 0
        max_turns = len(matrix) * len(matrix[0])
        while turns < max_turns:
            print(f'{i , j=} {matrix[i][j] = } {direction }')

            output.append(matrix[i][j])

            if direction == "right":
                j += 1
                if j >= width - 1 - time_around:
                    direction = "down"

            elif direction == "down":
                i += 1
                if i >= height - 1 - time_around:
                    direction = "left"
            elif direction == "left":
                j -= 1
                if j <= time_around:
                    direction = "up"
                    time_around += 1
            else:
                # direction up
                i -= 1
                if i <= time_around:
                    direction = "right"

            turns += 1
        return output


print(
    Solution().spiralOrder(
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    )
)

print([1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10])

# print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# print("=")
# print([1, 2, 3, 6, 9, 8, 7, 4, 5])

# print(Solution().spiralOrder([[3], [2]]))
# print("=")
# print([3, 2])

# print(Solution().spiralOrder([[3, 2]]))
# print("=")
# print([3, 2])

"""
54. Spiral Matrix
Medium
Topics
Companies
Hint
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

