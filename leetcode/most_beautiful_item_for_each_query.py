from typing import List

class Solution:
  def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
    items.sort()
    # for each cell calculate maximum beautifulnes
    for i in range(1, len(items)):
      items[i][1] = max(items[i-1][1], items[i][1])
    # print(f'{items}')
    ans = []
    for val in queries:
      ans.append(self.binarySearchRightMost(items, val))
    # print(f'{ans}')
    return ans
  
  def binarySearchRightMost(self, items, target):
    lo, hi = 0, len(items) - 1
    while lo < hi:
      mid = (lo + hi + 1) // 2
      if items[mid][0] > target:
        hi = mid - 1
      else:
        lo = mid
    return items[lo][1] if items[lo][0] <= target else 0
sol = Solution()
assert sol.maximumBeauty([[1,1],[1,1],[1,2],[1,1],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]) == [2,4,5,5,6,6]
