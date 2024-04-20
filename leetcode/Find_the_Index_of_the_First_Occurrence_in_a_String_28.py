
from re import search


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if found := search(needle, haystack):
            return found.span()[0]

        return -1


print(Solution().strStr(haystack="sadbutsad", needle="sad"), " = 0")
print(Solution().strStr(haystack="leetcode", needle="leetto"), " = -1")
print(Solution().strStr(haystack="hello", needle="ll"), " = 2")
"""
Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

"""

'''
other solution

class Solution:
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
'''

