# 1975. Maximum Matrix Sum

from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        negatives = 0
        lowest = float('inf')
        total = 0
        for row in matrix:
            for num in row:
                lowest = min(lowest, abs(num))
                if num <= 0:
                    negatives += 1
                total += abs(num)
        # print(f'{total = } {negatives = }, {lowest = }')
        if negatives % 2:
            total -= 2 * lowest
        return total
