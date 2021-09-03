class Solution:
  def validPalindrome(self, s: str) -> bool:
    # ss = ''.join(filter(lambda x : x.isalnum, s)).lower()
    ss = s
    l, r = 0, len(ss) - 1
    while (l < r):
      if ss[l] != ss[r]:
        return self.exactValidPalindrome(ss, l + 1, r) or self.exactValidPalindrome(ss, l, r - 1)
      l += 1
      r -= 1
    return True
  
  def exactValidPalindrome(self, ss: str, l: int, r: int) -> bool:
    while (l < r):
      if ss[l] != ss[r]:
        return False
      l += 1
      r -= 1
    return True

sol = Solution()
assert sol.validPalindrome('aba') == True
assert sol.validPalindrome('abca') == True
assert sol.validPalindrome('abccdba') == True
assert sol.validPalindrome('') == True
assert sol.validPalindrome('  ') == True
assert sol.validPalindrome('a') == True
assert sol.validPalindrome('ab') == True
assert sol.validPalindrome('raceacar') == True
assert sol.validPalindrome('abcdefdba') == False
