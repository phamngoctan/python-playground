class Solution:
  def maxVowels(self, s: str, k: int) -> int:
    count = 0
    res = 0
    for index, char in enumerate(s):
      if char in 'aeoui':
        count += 1
      if index - k >= 0:
        if s[index - k] in 'aeoui':
          count -= 1
      res = max(count, res)
    return res

sol = Solution()
assert sol.maxVowels("abciiidef", k = 3) == 3
assert sol.maxVowels("aeiou", k = 2) == 2
assert sol.maxVowels("leetcode", k = 3) == 2
assert sol.maxVowels("rhythms", k = 4) == 0
assert sol.maxVowels("tryhard", k = 4) == 1
assert sol.maxVowels("tryhard", k = 1) == 1
assert sol.maxVowels("aaaaaaaaaaaaaaaaaaaabbb", k = 3) == 3
