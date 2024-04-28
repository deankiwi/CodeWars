from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ...
        ring_size = len(matrix)
        if ring_size <= 1:
            return
        top_row = matrix[0][1:]

        passes = 0

        while ring_size > 1:

            # take left side and put it to top

            matrix[passes][1 + passes : -passes if passes else None] = [
                matrix[i + passes][passes] for i in range(ring_size - 1)
            ][::-1]

            # take bottom to left side
            for i in range(ring_size - 1):

                matrix[passes + i][passes] = matrix[-1 - passes][i + passes]

            # take the right and move it to the bottom
            matrix[-1 - passes][passes : -1 - passes] = [
                matrix[1 + i + passes][-1 - passes] for i in range(ring_size - 1)
            ][::-1]

            # move save top to right

            for i in range(ring_size - 1):

                matrix[1 + passes + i][-1 - passes] = top_row[i]

            passes += 1
            ring_size -= 2
            top_row = matrix[passes][1 + passes : -passes]


matrix = [[1, 2], [3, 4]]

Solution().rotate(matrix)
print(matrix)
print([[3, 1], [4, 2]])

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
Solution().rotate(matrix)
print(matrix)
print([[7, 4, 1], [8, 5, 2], [9, 6, 3]])

matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
print(matrix)
Solution().rotate(matrix)
print(matrix)
print([[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]])

"""
48. Rotate Image
Medium
Topics
Companies
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""
