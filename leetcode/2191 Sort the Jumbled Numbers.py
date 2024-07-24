

from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        def re_map(n):
            print(n)
            res = []
            for char in str(n):
                res.append(str(mapping[int(char)]))
            # print(f'{res = }')
            return int(''.join(res))

        return sorted(nums, key=re_map)

