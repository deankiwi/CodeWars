# Find N Unique Integers Sum up to Zero — LeetCode #1426 (Easy)
# URL: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
# Slug: find-n-unique-integers-sum-up-to-zero
# Difficulty: Easy
# Paid only: False
# Fetched: 2025-09-07

from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        result =  []
        for i in range(1,n//2+1):
            result.append(i)
            result.append(-i)
        if n%2 == 1:
            result.append(0)
        return result



