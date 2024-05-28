

import pprint
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0

        height = len(grid)
        width = len(grid[0])

        tracker = [[0] * width for _ in range(height)]

        island_id = {}
        connections = set()

        for j in range(height):
            # print(tracker)
            for i in range(width):
                # print(grid[j][i])
                # print(tracker)

                if grid[j][i] == "1":
                    # print('hit')
                    up = tracker[j - 1][i] if j > 0 else 0
                    left = tracker[j][i - 1] if i > 0 else 0

                    if up and left:

                        tracker[j][i] = min(up, left)
                        # TODO update island_id numbers
                        if up != left:
                            connections.add(tuple(sorted([up, left])))

                    elif up or left:

                        tracker[j][i] = island_id[max(up, left)]
                    else:
                        islands += 1
                        tracker[j][i] = islands
                        island_id[islands] = islands
        for connect in connections:
            island_id[connect[1]] = min(island_id[connect[1]], connect[0])
        count = 0
        for ids in island_id:
            if island_id[ids] == ids:
                count += 1

        return count


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]

print(Solution().numIslands(grid))

"""
200. Number of Islands
Medium
Topics
Companies
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

