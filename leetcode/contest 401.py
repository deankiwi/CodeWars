
# class Solution:
#     def numberOfChild(self, n: int, k: int) -> int:
#         cycle = n * 2 - 2
#         person = k % cycle
#         if person < n:
#             return person

#         return n - person % n - 2

# print(Solution().numberOfChild(5,6))

from collections import Counter
from math import comb
from typing import List


class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        max_num = max(rewardValues)
        count = Counter(rewardValues)
        count[max_num] -= 1
        # print(count)
        max_sequence = 0

        def dfs(count, x):
            # print(count)
            # print(x)
            nonlocal max_sequence
            if x >= max_num:
                # print('over max')
                return
            max_sequence = max(max_sequence, x)
            if max_sequence == max_num - 1:
                return
            for num in count:
                # print('try: ' + str(num))
                # print(count)
                if num > x and count[num]:
                    # print('reward added')
                    count[num] -= 1
                    dfs(count, x + num)
                    count[num] += 1

        dfs(count, 0)
        # print(max_sequence)
        return max_num + max_sequence

# print(Solution().maxTotalReward([1,6,4,3,2]))
# print(Solution().maxTotalReward([1,1,3,3]))
# print(Solution().maxTotalReward([1,5,4]))


print(comb(10,2))

# 2/4

