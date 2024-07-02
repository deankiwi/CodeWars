
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == '':
            return []
        keys = {
            '2' : ['a','b','c'],
            '3' : ['d','e','f'],
            '4' : ['g','h','i'],
            '5' : ['j','k','l'],
            '6' : ['m','n','o'],
            '7' : ['p','q','r', 's'],
            '8' : ['t','u','v'],
            '9' : ['w','x','y', 'z']
        }


        result = keys[digits[0]]

        for dig in digits[1:]:
            temp = []
            for letter in keys[dig]:
                for res in result:
                    temp.append(res+letter)
            result = temp
        return result


'''
cleaner solution

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                output.append(combination)
            else:
                for letter in phone_map[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])

        output = []
        backtrack("", digits)
        return output
'''

