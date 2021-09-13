class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False
    frequence = {}
    for i in range(len(s)):
      frequence[s[i]] = 1 if not s[i] in frequence else frequence[s[i]] + 1
      frequence[t[i]] = -1 if not t[i] in frequence else frequence[t[i]] - 1
    for i in frequence:
      if frequence[i] != None and frequence[i] != 0:
        return False
    return True
    
sol = Solution()
assert sol.isAnagram("anagram", "nagaram") == True
assert sol.isAnagram(s = "rat", t = "car") == False
assert sol.isAnagram(s = "t", t = "t") == True
assert sol.isAnagram(s = "tr", t = "rt") == True
assert sol.isAnagram(s = "a", t = "b") == False