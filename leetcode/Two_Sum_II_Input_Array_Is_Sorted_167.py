

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        see = {}
        i = 0
        j = len(numbers)-1
        while numbers[i] + numbers[j] != target or j == i:
            print(f"{i , j =}")
            if numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1

        return [i + 1, j + 1]


print(Solution().twoSum(numbers=[2, 7, 11, 15], target=9), " = [1,2]")
print(Solution().twoSum(numbers=[2, 3, 4], target=6), " = [1,3]")
print(
    Solution().twoSum(numbers=[1, 2, 30, 40, 50, 61, 70, 300, 1000], target=100),
    " = [3,7]",
)

"""
167. Two Sum II - Input Array Is Sorted
Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
"""

