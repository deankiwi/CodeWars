
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for price in prices[1:]:

            if price < min_price:
                min_price = price

            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit


arr = [7, 1, 5, 3, 6, 4]
print(arr)
print(Solution().maxProfit(arr))


arr = [7, 6, 4, 3, 1]
print(arr)
print(Solution().maxProfit(arr))

'''
design pattern the same but could have saved a few lines of code by using min and max

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
            
        return max_profit
'''

