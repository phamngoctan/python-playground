from typing import Counter


class Solution:
  def minWindow(self, s: str, t: str) -> str:
    if len(s) < len(t):
      return ''
    MAX_VALUE = 10**5 + 1
    freqT = Counter(t)
    # print(f'{freqT}')
    start = 0
    count = 0
    resLength = MAX_VALUE
    resRange = None
    freqS = {}
    for end, ch in enumerate(s):
      if ch not in freqS:
        freqS[ch] = 0
      freqS[ch] += 1
      if freqS[ch] == freqT[ch]:
        count += 1
      while count == len(freqT):
        if end - start + 1 < resLength:
          resLength = end - start + 1
          resRange = [start, end]
        charAtStart = s[start]
        if charAtStart in freqT and freqS[charAtStart] == freqT[charAtStart]:
          count -= 1
        freqS[charAtStart] -= 1
        start += 1
    # print(f'{resRange}')
    # print(f'{s[resRange[0]:resRange[1] + 1]}')
    return s[resRange[0]:resRange[1] + 1] if resLength != MAX_VALUE else ''

sol = Solution()
assert sol.minWindow('ADOBECODEBANC', 'ABC') == 'BANC'
assert sol.minWindow('AAAAAAAAAAAABBBBBCCC', 'ABC') == 'ABBBBBC'
assert sol.minWindow('a', 'aa') == ''
assert sol.minWindow('a', 'a') == 'a'
assert sol.minWindow('bA', 'a') == ''
