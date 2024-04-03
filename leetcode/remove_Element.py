

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        location = 0
        for i in nums:
            if i != val:
                nums[location] = i
                location += 1
        return location


test = Solution()

nums = [3,2,2,3]
print(test.removeElement(nums, 3))
print(nums)

nums = [0,1,2,2,3,0,4,2]
print(nums)
print(test.removeElement(nums, 2))
print(nums)

