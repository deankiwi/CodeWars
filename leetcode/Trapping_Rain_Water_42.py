
from typing import List


"""class Solution:
    def trap(self, height: List[int]) -> int:
        walls = {}  # {'level': 'location'}
        water = 0
        length = len(height)
        level = height[0]
        for loc in range(1, length):
            change = height[loc] - height[loc - 1]
            if change < 0:
                for chg_delta in range(height[loc - 1], height[loc], -1):
                    # print(f'{chg_delta = },{loc = }')
                    walls[chg_delta] = loc
            elif change > 0:
                for chg_delta in range(height[loc - 1] + 1, height[loc] + 1, 1):
                    # print(f'{chg_delta = },{loc = }')
                    if chg_delta in walls:
                        water += loc - walls[chg_delta]

        # print(walls)
        return water"""


class Solution:
    def trap(self, height: List[int]) -> int:
        walls = {height[0]: 1}  # {'level': 'location'}
        level_chg = [height[0]]  # heigh of each level
        water = 0
        length = len(height)

        for loc in range(1, length):
            height_from = height[loc - 1]
            height_to = height[loc]
            change = height_to - height_from
            if change < 0:  # going down
                walls[height_to] = loc + 1
                level_chg.append(height_to)

            elif change > 0:
                if level_chg:
                    last_level_chg = level_chg.pop()
                    level_added = height_from

                    while last_level_chg <= height_to:
                        water += (last_level_chg - level_added) * (
                            loc - walls[last_level_chg]
                        )
                        level_added = last_level_chg
                        if len(level_chg) > 0:
                            if level_chg[-1] <= height_to:
                                last_level_chg = level_chg.pop()
                            else:
                                water += (height_to - last_level_chg) * (
                                    loc - walls[level_chg[-1]]
                                )
                                break
                        else:
                            break
                walls[height_to] = loc + 1
                level_chg.append(height_to)

            else:
                walls[height_from] = loc + 1

        return water


print(Solution().trap([5, 5, 1, 7, 1, 1, 5, 2, 7, 6]), "= 23")
print(Solution().trap([2, 1, 0, 3]), "= 3")
print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), "= 6")
print(Solution().trap([4, 2, 0, 3, 2, 5]), "= 9")
height = [
    100000,
    0,
    99999,
    0,
    99998,
    0,
    99997,
    0,
    99996,
    0,
    99995,
    0,
    99994,
    0,
    99993,
    0,
    99992,
    0,
    99991,
    0,
    99990,
    0,
    99989,
    0,
    99988,
    0,
    99987,
    0,
    99986,
    0,
    99985,
    0,
    99984,
    0,
    99983,
    0,
    99982,
    0,
    99981,
    0,
    99980,
    0,
    99979,
    0,
    99978,
    0,
    99977,
    0,
    99976,
    0,
    99975,
    0,
    99974,
    0,
    99973,
    0,
    99972,
    0,
    99971,
    0,
    99970,
    0,
    99969,
    0,
    99968,
    0,
    99967,
    0,
    99966,
    0,
    99965,
    0,
    99964,
    0,
    99963,
    0,
    99962,
    0,
    99961,
    0,
    99960,
    0,
    99959,
]
print(Solution().trap(height), "= 4099139")


'''
better solution


Basically we are going to see whether we can trap the water or not.
within the given area.

Approach 1.(2 Pointer)
A basic idea comes into peoples mind if two walls are there and we want want to fill water within that wall we just have to fill the water till min of two wall right if it exceeds the value ,it will overflow.

So, we can set 2 pointers left_max,right_max and check which side is greater,if one side is greater iterate on other side because at the min side the water will be filled at its limit. and iterate till pointer is lower than the other one.

ex.height = [0,1,0,2,1,0,1,3,2,1,2,1]

left_max=0,right_max=1,count=0
amount of water is calculate using subtractring wall length with min(right_max,left_max);

iterate left_side.
count=0,left_max=0,right_max=1

iterate left_side.
count=0,left_max=1,right_max=1

iterate left_side.
count=1,left_max=1,right_max=1

iterate left_side.
count=2,left_max=2,right_max=1

iterate right_side.
count=2,left_side=2,right_side=2

iterate left_side.
count=3,left_side=2,right_side=2

iterate left_side.
count=5,left_side=2,right_side=2

iterate left_side.
count=5,left_side=3,right_side=2

iterate right_side.
count=6,left_side=3,right_side=2

iterate right_side.
count=6,left_side=3,right_side=2

so thats the amount of water is found.

Code


class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        left_max = height[0]
        sum = 0
        j = len(height) - 1
        right_max = height[j]
        while i < j:
            if left_max <= right_max:
                sum += left_max - height[i]
                i += 1
                left_max = max(left_max, height[i])
            else:
                sum += right_max - height[j]
                j -= 1
                right_max = max(right_max, height[j])
        return sum
'''
