
from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        count1 = Counter(nums1)
        count2 = Counter(nums2)

        result = []

        if len(count1) < len(count2):
            for num in count1:
                if num in count2:
                    result.extend([num] * min(count1[num], count2[num]))
        else:
            for num in count2:
                if num in count1:
                    result.extend([num] * min(count1[num], count2[num]))

        return result


print(Solution().intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))


