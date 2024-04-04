
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        majorityLength = len(nums) // 2

        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

            if count[i] > majorityLength:
                return i


arr = [3, 2, 3]
print(arr)
print(Solution().majorityElement(arr))
print(arr)

arr = [2, 2, 1, 1, 1, 2, 2]
print(arr)
print(Solution().majorityElement(arr))
print(arr)

"""
Used hash map to count
Could also us Moore Voting Algorithm 
"""

