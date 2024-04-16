

class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        string = ""
        for digit in roman:
            devisable = num // digit

            if devisable:
                string += roman[digit] * devisable
                num -= digit * devisable
        return string


print(Solution().intToRoman(3), " = III")
print(Solution().intToRoman(58), " = LVIII")
print(Solution().intToRoman(1994), " = MCMXCIV")

