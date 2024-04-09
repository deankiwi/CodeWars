

from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        time = 0
        tickets_needed = tickets[k]

        for index, ticket in enumerate(tickets):
            if index <= k:
                time += min(ticket, tickets_needed)

            else:
                time += min(ticket, tickets_needed - 1)

        return time


print(Solution().timeRequiredToBuy([2, 3, 2], 2), " == 6")
print(Solution().timeRequiredToBuy([5, 1, 1, 1], 0), " == 8")
print(Solution().timeRequiredToBuy([1, 5, 1, 1, 1], 1), " == 9")
print(Solution().timeRequiredToBuy([3, 2, 1], 1), " == 5")

