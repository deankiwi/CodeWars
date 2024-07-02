
# got 2/4 but last question passed a lot of test case

from collections import defaultdict
from typing import List


class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        width = 1
        height = 1
        balls = sorted([red, blue])
        while balls[1] >= width:
            balls[1] -= width
            width += 1
            if balls[0] >= width:
                height += 1
                width += 1
            else:
                break
        width = 1
        height2 = 1

        while balls[0] >= width:
            balls[0] -= width
            width += 1
            if balls[1] >= width:
                height2 += 1
                balls[1] -= width
                width += 1
            else:
                break
        return max([height, height2])

    def maximumLength(self, nums: List[int]) -> int:

        odds = nums[0] % 2
        evans = 1 - odds
        evan_odd = 1
        switch = nums[0] % 2

        for num in nums[1:]:
            if num % 2:
                # odd
                odds += 1
            else:
                evans += 1
            if num % 2 != switch:
                switch = num % 2
                evan_odd += 1

        return max([odds, evans, evan_odd])

    def minimumDiameterAfterMerge(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> int:

        first = self.solver(edges1)
        second = self.solver(edges2)

        print(f"{first = } {second = }")

        if first == second and first % 2 == 0:
            return first + 1

        return max([first, second])

    def solver(self, edges: List[List[int]]) -> int:
        # return the maximum length between two nodes
        maxx = 1

        seen = set()
        maped = defaultdict(list)

        for a, b in edges:
            maped[a].append(b)
            maped[b].append(b)

        def dfs(i) -> int:
            nonlocal maxx
            # return the max single road. if there are more than 1 road also check if it is on the longest track
            seen.add(i)
            biggest = []

            for j in maped[i]:
                if j not in seen:
                    biggest.append(dfs(j))

            if len(biggest) > 1:
                biggest.sort()
                maxx = max(maxx, biggest[-1] + biggest[-2] + 1)
            print(f"{biggest = }")
            if biggest:
                maxx = max(maxx, biggest[-1] + 1)
                return biggest[-1] + 1
            return 1

        dfs(0)

        return maxx


