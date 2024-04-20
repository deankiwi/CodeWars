
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for str in strs:
            ordered_str = "".join(sorted(str))

            if ordered_str in seen:
                seen[ordered_str].append(str)
            else:
                seen[ordered_str] = [str]

        return list(seen.values())


print(
    Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
    '= [["bat"],["nat","tan"],["ate","eat","tea"]]',
)
print(
    Solution().groupAnagrams([""]),
    '=  [[""]]',
)
print(
    Solution().groupAnagrams(["a"]),
    '=  [["a"]]',
)

"""
top solution was the same but used a default value for the default dict value to save a few lines of code 

class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())

"""

