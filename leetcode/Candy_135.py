

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        total = 0
        length = len(ratings)
        sweets = [1] * length
        for i in range(1, length):
            if ratings[i] > ratings[i - 1]:
                sweets[i] += sweets[i - 1]
        for i in range(length - 1, 0, -1):
            if ratings[i - 1] > ratings[i] and sweets[i - 1] <= sweets[i]:
                sweets[i - 1] = sweets[i] +1
        # print(ratings)
        print(sweets)
        return sum(sweets)


print(Solution().candy([1, 0, 2]), "= 5")
print(Solution().candy([1, 2, 2]), "= 4")
print(Solution().candy([1, 3, 2, 2, 1]), "= 7")
print(Solution().candy([1,6,10,8,7,3,2]), "= 18")


