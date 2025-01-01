from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        for _ in range(k):
            x = min(nums)
            index = nums.index(x)
            print(f'{x = }, {index = }')
            nums[index] = nums[index]*multiplier
            # nums = [x*multiplier] + nums[:index] + nums[index+1:]
        return nums


# for loop to k
#   x = min()
#   y = find(x)
#   nums = nums[y]* 2


# Input: nums = [2,1,3,5,6], k = 5, multiplier = 2

# Output: [8,4,6,5,6]

print(Solution().getFinalState(nums=[2, 1, 3, 5, 6], k=5, multiplier=2))
# print(Solution().getFinalState(nums=[2, 1, 3, 5, 6], k=2, multiplier=2))
