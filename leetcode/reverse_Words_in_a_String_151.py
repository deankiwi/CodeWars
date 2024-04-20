

import re


class Solution:
    def reverseWords(self, s: str) -> str:

        return " ".join(list(re.findall(r"[a-zA-Z0-9]+", s))[::-1])


print(Solution().reverseWords("the sky is blue"), ' ="blue is sky the"')
print(Solution().reverseWords("   the sky is    blue    "), ' ="blue is sky the"')
print(Solution().reverseWords("EPY2giL"), ' ="EPY2giL"')

"""
151. Reverse Words in a String
Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
"""

