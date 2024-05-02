

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0: return []
        output = []
        num_1 = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] + 1 != nums[i]:
                if num_1 != nums[i - 1]:
                    output.append(f"{num_1}->{nums[i-1]}")
                else:
                    output.append(str(nums[i - 1]))

                num_1 = nums[i]

            # TODO add in left result

        if num_1 != nums[-1]:
            output.append(f"{num_1}->{nums[-1]}")
        else:
            output.append(str(nums[- 1]))

        return output


print(Solution().summaryRanges([]), ' = []')
print(Solution().summaryRanges([0, 1, 2, 4, 5, 7]), ' = ["0->2","4->5","7"]')
print(Solution().summaryRanges([0, 2, 3, 4, 6, 8, 9]), ' = ["0","2->4","6","8->9"]')


"""
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
"""

