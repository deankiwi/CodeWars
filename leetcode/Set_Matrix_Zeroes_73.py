


from typing import List



class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = set() # vertical 
        n = set() # horizontal

        height = len(matrix)
        width = len(matrix[0])

        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 0:
                    m.add(i)
                    n.add(j)
        # change to zero horizontal
        for vert in m:
            for j in range(width):
                matrix[vert][j] = 0

        m_anti = [i for i in range(height) if i not in m]
        for j in n:
            for i in m_anti:
                matrix[i][j] = 0

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
expected_output = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
Solution().setZeroes(matrix)
print(matrix)
print(expected_output)
if matrix == expected_output:
    print('correct')
else:
    print('fail')




'''
73. Set Matrix Zeroes
Medium
Topics
Companies
Hint
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''

