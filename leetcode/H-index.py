
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()

        for i in range(1, len(citations) + 1):

            if i >= citations[-i]:
                # print(citations[-i], "cit", i, "index")
                return max(citations[-i], i-1)
        return len(citations)


print(Solution().hIndex([3, 0, 6, 1, 5]), 3)
print(Solution().hIndex([1, 3, 1]), 1)
print(Solution().hIndex([3, 3, 3]), 3)
print(Solution().hIndex([3, 3, 1]), 1)
print(Solution().hIndex([0, 3, 3]), 2)
print(Solution().hIndex([1,1,1,1,1,5]), 1)
print(Solution().hIndex([2]), 1)
print(Solution().hIndex([100]), 1)
print(Solution().hIndex([3,3]), 2)
print(Solution().hIndex([0,0,0,0,0,0]), 0)

