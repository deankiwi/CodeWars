
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        width = len(height) - 1
        i, j = 0, width
        area = 0
        while i < j:
            h = min(height[i], height[j])
            area = max(area, h * width)

            width -= 1
            if height[i] < height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
            else:
                width -=1
                i += 1
                j -= 1

        return area


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), " = 49")
print(Solution().maxArea([1,3,2,5,25,24,5]), " = 24")
"""
11. Container With Most Water
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
"""

