class Solution:
  def backspaceCompare(self, s: str, t: str) -> bool:
    s1 = self.extractHashFromString(s)
    t1 = self.extractHashFromString(t)
    return s1 == t1

  def extractHashFromString(self, s):
    s1 = []
    for i in range(len(s)):
      if s[i] == '#':
        s1 = s1[:-1]
      else:
        s1.append(s[i])
    return s1

sol = Solution()
assert sol.backspaceCompare('abc#d', 'abz#d') == True
assert sol.backspaceCompare('abc#d', 'abzaa###d') == True
assert sol.backspaceCompare('a##c', '#a#c') == True
assert sol.backspaceCompare('a#c', 'b') == False
assert sol.backspaceCompare('r', '#') == False
assert sol.backspaceCompare('#', 'r') == False
assert sol.backspaceCompare('#', '####') == True
