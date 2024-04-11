

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        length = len(gas)
        tank = min_tank = gas[0] - cost[0]
        min_tank_index = 1  

        for i in range(1, length):
            tank += gas[i] - cost[i]

            if min_tank > tank:
                min_tank = tank
                min_tank_index = (i + 1) % length

        if min_tank >= 0:
            return 0
        if tank >= 0:
            if length == 1:
                return 0
            return min_tank_index

        return -1


print(Solution().canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]), "= 3")
print(Solution().canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]), "= -1")
print(Solution().canCompleteCircuit(gas=[2], cost=[1]), "= 0")
print(Solution().canCompleteCircuit(gas=[1, 2], cost=[2, 1]), "= 1")
print(Solution().canCompleteCircuit(gas=[1, 2], cost=[2, 1]), "= 1")
print(Solution().canCompleteCircuit(gas=[2, 0, 0, 0], cost=[0, 1, 0, 0]), "= 0") # note this must be first possible solution


"""
had to update solution and testcase 39 was incorrect as it does not have uniqe solition `it is guaranteed to be unique` is not true, it wants first solution that works
overall fine though
"""


