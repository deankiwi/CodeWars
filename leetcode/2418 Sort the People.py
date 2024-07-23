

from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        comp = [[n,h] for n,h in zip(names, heights)]
        # print(comp)
        comp.sort(key=lambda x:x[1], reverse=True)
        # print(comp)
        return [x[0] for x in comp]


print(Solution().sortPeople(['a','b','c'],[1,3,2]))

