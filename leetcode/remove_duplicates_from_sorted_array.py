




class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 0: return 1

        lastIndexAdded = 0
        for index, number in enumerate(nums[1:]):
            if number != nums[lastIndexAdded]:
                lastIndexAdded += 1
                nums[lastIndexAdded] = number
        return lastIndexAdded + 1

test = Solution()

arr = [1,1,2]
print(arr)
print(test.removeDuplicates(arr))
print(arr)

arr = [0,0,1,1,1,2,2,3,3,4]
print(arr)
print(test.removeDuplicates(arr))
print(arr)

