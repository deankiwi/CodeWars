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
        heig_t = height
        heig_b = 0

        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    wid_l = min(wid_l, j)
                    wid_r = max(wid_r, j)
                    heig_t = min(heig_t, i)
                    heig_b = max(heig_b, i)

        area = (1 + wid_r - wid_l) * (1 + heig_b - heig_t)
        return area

    def maximumTotalCost(self, nums: List[int]) -> int:
        prev = nums[0]
        positive = True  # was the last one chosen a positive
        length = len(nums)
        for i in range(1, length):
            curr = nums[i]
            if i >= 0:
                prev += curr
                positive = True
            elif positive:
                prev -= curr
                positive = False
            elif i < length - 1 and curr >= nums[i + 1]:
                # check if the next number is greater than this one
                prev += curr
                positive = True
            elif curr >= nums[i - 1]:
                prev += curr
                positive = True
            else:
                prev = prev + 2 * nums[i - 1] - curr
                positive = False

        return prev


"""
3196. Maximize Total Cost of Alternating Subarrays
Medium
Topics
Companies
Hint
You are given an integer array nums with length n.

The cost of a 
subarray
 nums[l..r], where 0 <= l <= r < n, is defined as:

cost(l, r) = nums[l] - nums[l + 1] + ... + nums[r] * (−1)r − l

Your task is to split nums into subarrays such that the total cost of the subarrays is maximized, ensuring each element belongs to exactly one subarray.

Formally, if nums is split into k subarrays, where k > 1, at indices i1, i2, ..., ik − 1, where 0 <= i1 < i2 < ... < ik - 1 < n - 1, then the total cost will be:

cost(0, i1) + cost(i1 + 1, i2) + ... + cost(ik − 1 + 1, n − 1)

Return an integer denoting the maximum total cost of the subarrays after splitting the array optimally.

Note: If nums is not split into subarrays, i.e. k = 1, the total cost is simply cost(0, n - 1).

 

Example 1:

Input: nums = [1,-2,3,4]

Output: 10

Explanation:

One way to maximize the total cost is by splitting [1, -2, 3, 4] into subarrays [1, -2, 3] and [4]. The total cost will be (1 + 2 + 3) + 4 = 10.

Example 2:

Input: nums = [1,-1,1,-1]

Output: 4

Explanation:

One way to maximize the total cost is by splitting [1, -1, 1, -1] into subarrays [1, -1] and [1, -1]. The total cost will be (1 + 1) + (1 + 1) = 4.

Example 3:

Input: nums = [0]

Output: 0

Explanation:

We cannot split the array further, so the answer is 0.

Example 4:

Input: nums = [1,-1]

Output: 2

Explanation:

Selecting the whole array gives a total cost of 1 + 1 = 2, which is the maximum.

 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
