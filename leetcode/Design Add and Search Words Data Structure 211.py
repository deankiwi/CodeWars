
class WordDictionary:

    def __init__(self):
        self.root = {}
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr:
                curr[letter] = {}
            curr = curr[letter]
        curr['*'] = ''
        

    def search(self, word: str) -> bool:
        curr = self.root
        for letter in word:
            if letter == '.':
                for letter2 in curr:
                    newWord = word.replace('.',letter2,1)
                    if self.search(newWord):
                        return True
                else:
                    return False
            elif letter in curr:
                curr = curr[letter]
            else:
                return False
        if '*' in curr:
            return True
        return False

# 211. Design Add and Search Words Data Structure
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

