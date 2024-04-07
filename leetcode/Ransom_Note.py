

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for letter in ransomNote:
            if (index := magazine.find(letter)) != -1:

                magazine = magazine[:index] + magazine[index + 1 :]
            else:
                return False

        return True



print(Solution().canConstruct("a", "b"), "false")
print(Solution().canConstruct("aa", "ab"), "false")
print(Solution().canConstruct("aaaaa", "aabbbbb"), "true")


'''
My solution is good, another option could have been:

Hashmap
another solution was using the Counter class (turns each character into a string)
Counter & Counter => returns object of matching counter

from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        st1, st2 = Counter(ransomNote), Counter(magazine)
        if st1 & st2 == st1:
            return True
        return False
'''

