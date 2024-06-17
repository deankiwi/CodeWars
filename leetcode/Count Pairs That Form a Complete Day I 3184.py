
from typing import List
import math


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        rem = [0] * 24

        for hour in hours:
            diff = hour % 24
            rem[diff] += 1
        count = 0

        if rem[0] >= 2:
            n = rem[0]
            count += int(math.factorial(n) / (2 * math.factorial(n - 2)))

        if rem[12] >= 2:
            n = rem[12]
            count += int(math.factorial(n) / (2 * math.factorial(n - 2)))

        for i in range(1, 12):
            n = rem[i]
            m = rem[-i]
            count += n * m

        return count


# print(Solution().countCompleteDayPairs([12, 12, 30, 24, 24]))
# print(Solution().countCompleteDayPairs([72,48,24,3]))
print(Solution().countCompleteDayPairs([48, 48, 15, 12, 12, 48, 48]))

