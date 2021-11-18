from typing import List

class Solution:
  def findAnagrams(self, s: str, p: str) -> List[int]:
    if len(s) < len(p):
      return []
    freqS = {}
    freqP = {}
    for i in range(26):
      freqS[chr(ord('a') + i)] = 0
      freqP[chr(ord('a') + i)] = 0
    for c in p:
      freqP[c] += 1
    
    count = 0
    res = []
    for end, c in enumerate(s):
      freqS[c] += 1
      count += 1
      if count > len(p):
        freqS[s[end - count + 1]] -= 1
        count -= 1
      if freqS == freqP:
        res.append(end - count + 1)
    # print(f'{res}')
    return res
sol = Solution()
assert sol.findAnagrams("cbaebabacd", p = "abc") == [0,6]
assert sol.findAnagrams("abab", p = "ab") == [0,1,2]
assert sol.findAnagrams("abab", p = "a") == [0,2]
assert sol.findAnagrams("abab", p = "ababa") == []
