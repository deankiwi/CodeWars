
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:

        c = Counter(s)
        ans = 0
        odd = False
        for key in c:
            count = c[key]
            if count % 2:
                odd = True
                ans += count - 1
            else:
                ans += count
        if odd:
            ans += 1
        return ans


print(Counter("hello"))
"""
409. Longest Palindrome
Easy
Topics
Companies
Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindrome
 that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
"""
