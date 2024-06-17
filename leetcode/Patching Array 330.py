
from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # go through an find the missing gaps
        # then if the sum of all the numbers isn't greater than n add sum + 1 until greater
        patch = 0
        total = 0

        for num in nums:
            while n > total and num > total + 1:
                patch += 1
                total += total + 1
            else:
                total += num
                if total >= n:
                    return patch
        while total < n:
            patch += 1
            total += total + 1

        return patch



# print(Solution().minPatches(nums=[1, 5, 10], n=20))
# print(Solution().minPatches(nums=[1, 2, 2], n=5))
# print(Solution().minPatches(nums=[1, 7, 21], n=12))
print(Solution().minPatches(nums=[1,2,2,6,34,38,41,44,47,47,56,59,62,73,77,83,87,89,94], n=12))

"""
330. Patching Array
Hard
Topics
Companies
Given a sorted integer array nums and an integer n, add/patch elements to the array such that any number in the range [1, n] inclusive can be formed by the sum of some elements in the array.

Return the minimum number of patches required.

 

Example 1:

Input: nums = [1,3], n = 6
Output: 1
Explanation:
Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.
Example 2:

Input: nums = [1,5,10], n = 20
Output: 2
Explanation: The two patches can be [2, 4].
Example 3:

Input: nums = [1,2,2], n = 5
Output: 0
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 104
nums is sorted in ascending order.
1 <= n <= 231 - 1
"""


