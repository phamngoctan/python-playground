class WordDictionary:
    def __init__(self):
        self.wordLibs = [None] * 26
        self.ending = False

    def addWord(self, word: str) -> None:
        def addHelper(word, parent):
            if not word:
                return
            current = ord(word[0]) - ord('a')
            if parent.wordLibs[current] == None:
                parent.wordLibs[current] = WordDictionary()
            if len(word) == 1:
                parent.wordLibs[current].ending = True
            addHelper(word[1:], parent.wordLibs[current])
        addHelper(word, self)

    def search(self, word: str) -> bool:
        def searchHelper(word, parent):
            if not word:
                return False
            if len(word) == 1 and word[0] == '.':
                return True if any(element and element.ending for element in parent.wordLibs) else False
            
            current = ord(word[0]) - ord('a')
            if len(word) == 1:
                return parent.wordLibs[current] != None and parent.wordLibs[current].ending == True
            
            if word[0] == '.':
                for i in range(26):
                    if parent.wordLibs[i]:
                        if searchHelper(word[1:], parent.wordLibs[i]):
                            return True
            else:
                if parent.wordLibs[current]:
                    if searchHelper(word[1:], parent.wordLibs[current]):
                        return True
            return False
        return searchHelper(word, self)


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord('at')
obj.addWord('and')
obj.addWord('an')
obj.addWord('add')
obj.addWord('bat')
assert obj.search('a') == False
assert obj.search('b.') == False