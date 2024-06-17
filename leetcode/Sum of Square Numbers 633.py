
from math import sqrt, isqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        low = 0
        high = isqrt(c)

        if c == high**2:
            return True

        while low < high:

            diff = low**2 + high**2 - c
            if diff == 0:
                return True
            elif diff < 0:

                chg = low**2 - diff

                if isqrt(chg) ** 2 == chg:
                    return True
                low += 1
                high -= 1
            else:
                chg = high**2 - diff
                if isqrt(chg) ** 2 == chg:
                    return True
                low += 1
                high -= 1

        return False


print(Solution().judgeSquareSum(61))

"""
633. Sum of Square Numbers
Medium
Topics
Companies
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

 

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:

Input: c = 3
Output: false
 

Constraints:

0 <= c <= 231 - 1
"""

