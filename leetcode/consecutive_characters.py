from typing import Counter

class Solution:
  def maxPower(self, s: str) -> int:
    maxP = 0
    i, j = 0, 0
    while i < len(s):
      while j < len(s) and s[j] == s[i]:
        j += 1
        maxP = max(maxP, j - i)
      i = j
    return maxP
        
      
sol = Solution()
assert sol.maxPower("leetcode") == 2
assert sol.maxPower("abbcccddddeeeeedcba") == 5
assert sol.maxPower("a") == 1
assert sol.maxPower("triplepillooooow") == 5
assert sol.maxPower("tourist") == 1
