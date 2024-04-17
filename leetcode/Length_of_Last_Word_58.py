

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for letter in s[::-1]:

            if letter == " " and count:
                return count
            elif letter != " ":
                count += 1
        return count


print(Solution().lengthOfLastWord(s="   fly me   to   the moon  "), " = 4")

