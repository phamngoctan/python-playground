class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    # if len(s) <= 1:
    #   return len(s)

    l, r = -1, 0
    maxLength = 0
    freq = {}
    while r < len(s):
      # print(f'{l} -> {r}')
      if s[r] in freq:
        # pass
        if freq[s[r]] >= l:
          l = freq[s[r]]
        else:
          maxLength = max(r - l, maxLength)
        freq[s[r]] = r
      else:
        maxLength = max(r - l, maxLength)
        freq[s[r]] = r
        # print(f'{freq}')
      r += 1
      # print(f'{maxLength}')
      # print('--------')
    return maxLength

sol = Solution()
assert sol.lengthOfLongestSubstring('abcabcbb') == 3
assert sol.lengthOfLongestSubstring('') == 0
assert sol.lengthOfLongestSubstring('a') == 1
assert sol.lengthOfLongestSubstring('pwwkew') == 3
assert sol.lengthOfLongestSubstring('abcbdaac') == 4