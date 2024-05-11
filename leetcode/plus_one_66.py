

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits) - 1, -1, -1):
            print(i)
            if digits[i] != 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0

        if digits[0] == 0:
            digits[0] = 1
            digits.append(0)

        return digits


print(Solution().plusOne([1, 2, 3]))
print(Solution().plusOne([9]))

