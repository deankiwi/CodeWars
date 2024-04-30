

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = {"(", "{", "["}
        close = {")": "(", "}": "{", "]": "["}
        for bracket in s:
            if bracket in open:
                stack.append(bracket)
            elif len(stack) == 0:
                return False

            elif not stack.pop() == close[bracket]:
                return False

        return len(stack) == 0


print(Solution().isValid("()"), " = True")
print(Solution().isValid("(]"), " = False")
print(Solution().isValid("([])"), " = True")

