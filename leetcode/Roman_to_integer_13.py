

class Solution:
    def romanToInt(self, s: str) -> int:
        key = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        biggest_digit = 0
        for symbol in s[::-1]:
            if key[symbol] < biggest_digit:
                total -= key[symbol]
            else:
                total += key[symbol]
                biggest_digit = key[symbol]

        return total


print(Solution().romanToInt("III"), "= 3")
print(Solution().romanToInt("LVIII"), "= 58")
print(Solution().romanToInt("MCMXCIV"), "= 1994")

