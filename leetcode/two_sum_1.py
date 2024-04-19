

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ...
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


print(Solution().twoSum([2, 7, 11, 15], 9), " = [0,1]")
print(Solution().twoSum([3, 2, 4], 6), " = [1,2]")
print(Solution().twoSum([0, 1], 6), " = [0,1]")


"""
use Hashmap

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []  # No solution found
"""


