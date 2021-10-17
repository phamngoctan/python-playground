class TrieNode:
  def __init__(self) -> None:
    self.end = False
    self.keys = {}

class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word: str) -> None:
    def insertHelper(node, word):
      if len(word) == 0:
        node.end = True
        return
      elif not word[0] in node.keys:
        node.keys[word[0]] = TrieNode()
        insertHelper(node.keys[word[0]], word[1:])
      else:
        insertHelper(node.keys[word[0]], word[1:])
    insertHelper(self.root, word)

  def search(self, word: str) -> bool:
    def searchHelper(node, word):
      if len(word) == 0:
        return node.end
      elif not word[0] in node.keys:
        return False
      else:
        return searchHelper(node.keys[word[0]], word[1:])
    return searchHelper(self.root, word)
  
  def startsWith(self, prefix: str) -> bool:
    def startsWithHelper(node, word):
      if len(word) == 0:
        return True
      elif not word[0] in node.keys:
        return False
      else:
        return startsWithHelper(node.keys[word[0]], word[1:])
    return startsWithHelper(self.root, prefix)



# Your Trie object will be instantiated and called as such:
word = 'dog'
obj = Trie()
obj.insert(word)
print(f'{obj}')
print(f'{obj.search(word)}')
print(f'{obj.search("cat")}')
print(f'{obj.startsWith("do")}')
print(f'{obj.startsWith("og")}')

obj.insert("app")
obj.insert("apple")
obj.insert("beer")
obj.insert("add")

#["Trie","insert","insert","insert","insert","insert","insert","search","search","search","search","search","search","search","search","search","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith"]
# [[],["app"],["apple"],["beer"],["add"],["jam"],["rental"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"]]