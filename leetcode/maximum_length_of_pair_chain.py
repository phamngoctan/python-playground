from typing import List

class Solution:
  def findLongestChain(self, pairs: List[List[int]]) -> int:
    '''
    Keyword: Sort the pairs by pair[1] (tail).
    pick smaller tail which has a better opportunity to append more future pairs
    '''
    pairs.sort(key = lambda x: x[1])
    # print(f'{pairs}')
    MIN_VAL = -1007
    ans = 0
    previousEnd = MIN_VAL
    for start, end in pairs:
      if previousEnd < start:
        ans += 1
        previousEnd = end
    # print(f'{ans}')
    return ans
sol = Solution()
assert sol.findLongestChain([[1,2],[2,3],[3,4]]) == 2
assert sol.findLongestChain([[1,2],[7,8],[4,5]]) == 3
assert sol.findLongestChain([[1,8],[2,3],[5,6]]) == 2
assert sol.findLongestChain([[1,8],[2,3]]) == 1
assert sol.findLongestChain([[1,8],[2,4],[3,5]]) == 1
