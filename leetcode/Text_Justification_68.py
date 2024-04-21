

from pprint import pprint
from typing import List


class Solution:

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        wordsList = []
        backIndex = 0
        currentWidth = 0
        for i in range(len(words)):
            word = words[i]
            w_length = len(word)
            num_of_words = i - backIndex
            # print(f"{word, currentWidth , w_length , num_of_words =}")
            if currentWidth + w_length + num_of_words > maxWidth:

                if num_of_words == 1:
                    wordsList.append(
                        words[backIndex] + " " * (maxWidth - len(words[backIndex]))
                    )
                    # print(f"{maxWidth - w_length =} {w_length , maxWidth = }")
                else:

                    padding = (maxWidth - currentWidth) // (num_of_words - 1)
                    # print(
                    #     f"{padding = } {w_length = } {currentWidth = } {num_of_words = }"
                    # )
                    # print(f"{maxWidth , currentWidth , num_of_words=}")
                    wordsList.append((" " * padding).join(words[backIndex:i]))
                    if len(wordsList[-1]) < maxWidth:
                        # print("hit  !!!!!!")
                        # print(f'{1 + maxWidth - len(wordsList[-1]) = }')
                        wordsList[-1] = wordsList[-1].replace(
                            " ", "  ",  ( maxWidth - len(wordsList[-1]))
                        )
                        # print(f"{num_of_words, wordsList = }")

                backIndex = i
                currentWidth = w_length
            else:
                currentWidth += w_length

        if backIndex < len(words):
            # TODO add in left justified
            wordsList.append(" ".join(words[backIndex:]))
            wordsList[-1] = wordsList[-1] + " " * (maxWidth - len(wordsList[-1]))

        return wordsList


print(
    Solution().fullJustify(
        [
            "a",
            "b",
            "c",
            "b",
            "a",
            "bob",
            "a",
            "b",
            "a",
            "b",
        ],
        4,
    )
)
pprint(
    Solution().fullJustify(
        ["This", "is", "an", "example", "of", "text", "justification."], 16
    )
)
print(["This    is    an", "example  of text", "justification.  "])
print(
    Solution().fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16)
)
print(["What   must   be", "acknowledgment  ", "shall be        "])
print(
    Solution().fullJustify(
        words=[
            "Science",
            "is",
            "what",
            "we",
            "understand",
            "well",
            "enough",
            "to",
            "explain",
            "to",
            "a",
            "computer.",
            "Art",
            "is",
            "everything",
            "else",
            "we",
            "do",
        ],
        maxWidth=20,
    )
)
print(
    [
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  ",
    ]
)

"""

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
"""


'''
other solution used same design pattern to myself apart from adding in space in which as used a far simpler solution of adding spacing in a 
round robbin type way


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
            
        result, current_list, num_of_letters = [],[], 0
        # result -> stores final result output
        # current_list -> stores list of words which are traversed but not yet added to result
        # num_of_letters -> stores number of chars corresponding to words in current_list
        
        for word in words:
            
            # total no. of chars in current_list + total no. of chars in current word
            # + total no. of words ~= min. number of spaces between words
            if num_of_letters + len(word) + len(current_list) > maxWidth:
                # size will be used for module "magic" for round robin
                # we use max. 1 because atleast one word would be there and to avoid modulo by 0
                size = max(1, len(current_list)-1)
                
                for i in range(maxWidth-num_of_letters):
                    # add space to each word in round robin fashion
                    index = i%size
                    current_list[index] += ' ' 
                
                # add current line of words to the output
                result.append("".join(current_list))
                current_list, num_of_letters = [], 0
            
            # add current word to the list and add length to char count
            current_list.append(word)
            num_of_letters += len(word)
        
        # form last line by join with space and left justify to maxWidth using ljust (python method)
        # that means pad additional spaces to the right to make string length equal to maxWidth
        result.append(" ".join(current_list).ljust(maxWidth))
        
        return result
'''
