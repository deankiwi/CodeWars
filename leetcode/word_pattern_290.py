

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split(" ")
        pattern_index = []
        words_index = []
        for pat in pattern:
            pattern_index.append((pattern.index(pat)))
        for word in words:
            words_index.append(words.index(word))

        return pattern_index == words_index


print(Solution().wordPattern("abba", "dog cat cat dog"), " = True")
print(Solution().wordPattern("abba", "dog cat cat fish"), " = False")

