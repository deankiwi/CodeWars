
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        buy = prices[0]
        for price in prices[1:]:
            if price > buy:
                profit += price - buy
                buy = price
            else:
                buy = price
        return profit


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit([7,6,4,3,1]))
print(Solution().maxProfit([1,2,3]))

