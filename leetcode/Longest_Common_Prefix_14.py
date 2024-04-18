
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        matches = strs[0]
        for word in strs[1:]:
            for i in range(len(matches), 0, -1):

                if matches[:i] == word[:i]:
                    matches = matches[:i]
                    break
                elif i == 1:
                    return ""  # no matches found
        return matches


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]), " = fl")
print(Solution().longestCommonPrefix(["dog", "racecar", "car"]), ' = ""')
print(
    Solution().longestCommonPrefix(["flower", "flower", "flower", "flower"]),
    " = flower",
)

'''

other solutions

sort words first then look at last and first word

class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans=""
        v=sorted(v)
        first=v[0]
        last=v[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 

compare each letter across all words one by one

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs):
            return ''
        
        i = 0
        for i, chars in enumerate(zip(*strs), 1):
            if len(set(chars)) != 1:
                i -= 1
                break
        
        return strs[0][:i]
'''

