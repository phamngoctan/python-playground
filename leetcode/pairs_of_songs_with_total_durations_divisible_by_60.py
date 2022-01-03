from typing import List

class Solution:
  def numPairsDivisibleBy60(self, time: List[int]) -> int:
    prefixHash = {}
    ans = 0
    for t in time:
      t = t % 60
      if ((60 - t) % 60) in prefixHash:
        ans += prefixHash[((60 - t) % 60)] # handle edge case [60,60,60]
      prefixHash.setdefault(t, 0)
      prefixHash[t] += 1
    return ans
  
  def numPairsDivisibleBy60_myOriginalIdea(self, time: List[int]) -> int:
    newTime = []
    for t in time:
      newTime.append(t % 60)
    prefixHash = {}
    # prefixHash[0] = 0
    ans = 0
    for i, t in enumerate(newTime):
      if ((60 - t) % 60) in prefixHash:
        ans += prefixHash[((60 - t) % 60)]
      prefixHash.setdefault(t, 0)
      prefixHash[t] += 1
    # print(f'{ans}')
    return ans
sol = Solution()
assert sol.numPairsDivisibleBy60([30,20,150,100,40]) == 3
assert sol.numPairsDivisibleBy60([60,60,60]) == 3