
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_cons = 0
        seen = {}  # store {num : end of consecutive at time placed}

        for num in nums:
            if num not in seen:

                above = seen[num + 1] if num + 1 in seen else num
                below = seen[num - 1] if num - 1 in seen else num
                max_cons = max(max_cons, above - below + 1)
                # check to see if num is at bottom or top of sequence
                seen[num] = num
                seen[above] = below
                seen[below] = above

        return max_cons


print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]), " = 4")
print(Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), " = 9")

"""
Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""


