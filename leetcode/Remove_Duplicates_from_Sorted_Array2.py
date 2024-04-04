

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        length = len(nums)
        if length <= 2:
            return length

        index = 1
        for i in range(2, length):
            if nums[i] != nums[index] or nums[i] != nums[index - 1]:
                index += 1
                nums[index] = nums[i]
        return index+1


arr = [1, 1, 1, 2, 2, 3]
print(arr)
print(Solution().removeDuplicates(arr))
print(arr)

arr = [0,0,1,1,1,1,2,3,3]
print(arr)
print(Solution().removeDuplicates(arr))
print(arr)


'''
comments, I did not need to check for nums[i] != nums[index] 
as it is always a sorted list therefore 
if nums[i] == nums[index-1] is true
    nums[i] == nums[index] will always be true
'''

