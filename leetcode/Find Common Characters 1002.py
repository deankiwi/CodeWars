

from collections import Counter
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])

        for word in words[1:]:
            matches = Counter()
            for letter in word:
                if letter in common:
                    common[letter] -= 1
                    matches[letter] += 1
                    if common[letter] == 0:
                        del common[letter]
                        if len(common) == 0:
                            break
            if len(matches) == 0:
                return []
            common = matches
        res = []
        for letter in common:
            for count in range(common[letter]):
                res.append(letter)
        return res

print(Solution().commonChars(["bella","label","roller"]))

"""
1002. Find Common Characters
Easy
Topics
Companies
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
"""

