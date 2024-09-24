

from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # make a tri from arr1
        # keep a value for max value
        # go through each value of arr2 to find max value
        commonVal = 0 
        arr1Trie = {}
        for val in arr1:
            curr = arr1Trie
            for i in str(val):
                if i not in curr:
                    curr[i] = {}
                curr = curr[i]
        for val in arr2:
            curr = arr1Trie
            count = 0
            for i in str(val):
                if i not in curr:
                    break
                curr = curr[i]
                count += 1
            commonVal = max (commonVal, count)


        return commonVal


