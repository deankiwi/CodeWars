

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        s_count = Counter(s[: len(t)])
        t_count = Counter(t)

        front = len(t)

        min_word = len(s) + 1

        if (t_count - s_count).total() == 0:

            word = s[0:front]
        else:
            word = ""

        for back in range(0, len(s) - len(t) + 1):

            while front < len(s) and ((t_count - s_count).total() != 0):

                s_count[s[front]] += 1
                front += 1

            if (t_count - s_count).total() == 0:
                if front - back < min_word:
                    min_word = front - back
                    word = s[back:front]

            s_count[s[back]] -= 1

        return word


print(Solution().minWindow("ADOBECODEBANC", "ABC"), " = BANC")
print(Solution().minWindow("abc", "aa"), ' = ""')
print(Solution().minWindow("a", "a"), " = a")
print(Solution().minWindow("aa", "a"), " = a")
print(Solution().minWindow("ba", "a"), " = a")


"""

76. Minimum Window Substring
Hard
Topics
Companies
Hint
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?

"""


"""
better solution rather than checking through the whole hash values keep value to 
store how many matches we 'need' and how many we 'have' with the window

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
"""

