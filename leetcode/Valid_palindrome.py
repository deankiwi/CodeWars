
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = re.sub(r'[^a-z0-9]+','',s.lower())

        if s == s[::-1]:
            return True
        else:
            return False





test = Solution()

print(test.isPalindrome('A man, a plan, a canal: Panama'))
print(test.isPalindrome(''))
print(test.isPalindrome('hello'))
print(test.isPalindrome('0p'))


'''
Faster solution

Will only iterate over the solution once and break earlier if it is false

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False

        return True
            

'''

