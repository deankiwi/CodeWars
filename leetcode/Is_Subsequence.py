

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        character_index = 0
        length = len(s)
        if length == 0: return True
        for char in t:
            if s[character_index] == char:

                character_index += 1
                if length == character_index:
                    return True


        return False


print(Solution().isSubsequence("abc", "ahbgdc"))


'''
clearer solution, same design pattern

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
'''

