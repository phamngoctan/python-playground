class Solution:
  def detectCapitalUse(self, word: str) -> bool:
    return word.isupper() or word.islower() or word.istitle()
  
  def detectCapitalUse_borrow1(self, word: str) -> bool:
    return word[1:]==word[1:].lower() or word==word.upper()
  
  def detectCapitalUse_myOwnSolution(self, word: str) -> bool:
    # if len(word) == 1:
    #   return True
    
    firstWordUpper = ord(word[0]) < 92
    countLowerCase = 0
    for c in word:
      if ord(c) >= 97: # upper case
        countLowerCase += 1
    return countLowerCase == 0 or countLowerCase == len(word) or (countLowerCase == len(word) - 1 and firstWordUpper)

sol = Solution()
assert sol.detectCapitalUse("USA") == True
assert sol.detectCapitalUse("leetcode") == True
assert sol.detectCapitalUse("Google") == True
assert sol.detectCapitalUse("FlaG") == False
assert sol.detectCapitalUse("a") == True
assert sol.detectCapitalUse("A") == True
assert sol.detectCapitalUse("Aa") == True
assert sol.detectCapitalUse("aA") == False
assert sol.detectCapitalUse("aAAAA") == False
