
from typing import List

from collections import defaultdict


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        length = len(words)
        w_length = len(words[0])
        sub_string_len = length * w_length
        output = []
        word_count = defaultdict(int)
        temp_word_count = defaultdict(int)

        for word in words:
            word_count[word] += 1

        # print(words)

        dis_from_end = len(s) - length * w_length

        for i in range(0, dis_from_end + 1):

            # print(f"{s[i:i+sub_string_len ] = }")

            for j in range(i, i + sub_string_len, w_length):
                # print(f"{i,j = }")
                check_word = s[j : j + w_length]
                # print(f"{check_word = }")
                if word_count[check_word]:
                    word_count[check_word] -= 1
                    temp_word_count[check_word] += 1

                else:

                    break
            else:
                # print("match")
                output.append(i)
            for key in temp_word_count:
                word_count[key] += temp_word_count[key]
            temp_word_count.clear()

        return output


print(
    Solution().findSubstring(s="abcde", words=["b", "c", "d"]),
    " == ",
    [1],
)
print(
    Solution().findSubstring(s="barfoofoobarthefoobarman", words=["bar", "foo", "the"]),
    " == ",
    [6, 9, 12],
)
print(
    Solution().findSubstring(
        s="wordgoodgoodgoodbestword", words=["word", "good", "best", "word"]
    ),
    " == ",
    [],
)


"""
30. Substring with Concatenation of All Words
Hard

You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

 

Constraints:

1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.
"""


"""
better solution

as all words are same length you can start 

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or not s:
            return []

        word_length = len(words[0])
        total_length = word_length * len(words)
        word_count = {}

        # Create a frequency map for words
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        result = []

        # Check each possible window in the string
        for i in range(word_length):
            left = i
            count = 0
            temp_word_count = {}

            for j in range(i, len(s) - word_length + 1, word_length):
                word = s[j:j + word_length]
                if word in word_count:
                    temp_word_count[word] = temp_word_count.get(word, 0) + 1
                    count += 1

                    while temp_word_count[word] > word_count[word]:
                        left_word = s[left:left + word_length]
                        temp_word_count[left_word] -= 1
                        left += word_length
                        count -= 1

                    if count == len(words):
                        result.append(left)
                else:
                    temp_word_count.clear()
                    count = 0
                    left = j + word_length

        return result
"""

