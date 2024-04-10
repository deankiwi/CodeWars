

from math import prod
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = nums.count(0)
        if zeros == 0:
            sum = prod(nums)
            return [sum // i for i in nums]
        elif zeros == 1:
            index = nums.index(0)

            sum = prod(nums[:index] + nums[index + 1 :])

            return [0] * (index) + [sum] + [0] * (len(nums) - index - 1)
        else:
            return [0] * len(nums)


print(Solution().productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])
print(Solution().productExceptSelf([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])
print(Solution().productExceptSelf([-1, 1, 0, 0]), [0, 0, 0, 0])


'''
better solution
- come at the array at either end keep track of product at each end


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        sol=[1]*length
        pre = 1
        post = 1
        for i in range(length):
            sol[i] *= pre
            pre = pre*nums[i]
            sol[length-i-1] *= post
            post = post*nums[length-i-1]
        return(sol)
'''

