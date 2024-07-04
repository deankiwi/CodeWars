
from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        # find 4 smallest
        # find 4 largest
        # try small small small
        # try small small large
        # try small large large
        # try large large large

        smallest = sorted(nums[:4])
        largest = sorted(nums[:4],reverse=True)


        for num in nums[4:]:

            if num < smallest[-1]:
                smallest.append(num)
                smallest.sort()
                if len(smallest) == 5:
                    smallest.pop()
            
            if num > largest[-1]:
                largest.append(num)
                largest.sort(reverse=True)
                if len(largest) == 5:
                    largest.pop()
        
        # print(f'{smallest = } {largest = }')
        
        choices = []
        for i in range(4):
            choices.append(largest[i] - smallest[3-i])
        # print(choices)
        
        return min(choices)
    
