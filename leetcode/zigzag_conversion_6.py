

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        down = True
        index = 0
        matrix = [[] for _ in range(numRows)]
        for l in s:
            matrix[index].append(l)
            if down:
                if index < numRows - 1:
                    index += 1
                else:
                    index -= 1
                    down = False
            else:
                if index > 0:
                    index -= 1
                else:
                    index += 1
                    down = True

        return "".join(''.join(i) for i in matrix)


print(Solution().convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR", sep="\n")

"""
6. Zigzag Conversion

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"

"""

