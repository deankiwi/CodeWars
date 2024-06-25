

from turtle import width
from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:

        averages = []
        nums.sort()

        for i in range(len(nums)):
            avg = (nums[i] + nums[-i - 1]) / 2
            averages.append(avg)

        return min(averages)

    def minimumArea(self, grid: List[List[int]]) -> int:

        height = len(grid)
        width = len(grid[0])
        # make box with left, right, top and bottom
        wid_l = width
        wid_r = 0
        heig_t = 0
        heig_b = height

        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    wid_l = min(wid_l, j)
                    wid_r = max(wid_r, j)
                    heig_t = min(heig_t, i)
                    heig_b = max(heig_b, i)
        if wid_r:
            area = (wid_r - wid_l) * (heig_b - heig_t)
            return area
        return 0

