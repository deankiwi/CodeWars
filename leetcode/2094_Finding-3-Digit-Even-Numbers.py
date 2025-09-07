# 2094. Finding 3-Digit Even Numbers

from collections import Counter, defaultdict
from statistics import median
from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:

        count_nums = Counter(digits)

        results = []
        for i in range(100, 999, 2):
            count_2 = Counter([int(x) for x in str(i)])
            
            for num in count_2:

                if num not in count_nums or count_2.get(num) > count_nums.get(num):
                    break
            else:
                results.append(i)

        return results


print(Solution().findEvenNumbers([2, 2, 8, 8, 2]))


class MyClass():
    def __init__(self):
        self.total_num_of_numbers = 0
        self.median = None
        self.count = defaultdict(int)
    def add(self,num):
        self.total_num_of_numbers += 1
        self.count[num] += 1
        if self.median != None or self.median != num:
