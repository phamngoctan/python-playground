from typing import List

class Solution:
  def minSwapsCouples(self, row: List[int]) -> int:
    N = len(row)//2
    global swap
    swap = 0
    parent = [i for i in range(N)]
    def findSet(u):
      while u != parent[u]:
        u = parent[u]
      return u
    def unionSet(u, v):
      global swap
      uParent = findSet(u)
      vParent = findSet(v)
      if uParent != vParent:
        parent[uParent] = vParent
        swap += 1
    for i in range(N):
      u = row[i * 2] // 2 # get the couple id (0,1) will be couple 0, (1,2) will be couple 1
      v = row[i * 2 + 1] // 2
      unionSet(u, v)
    return swap

sol = Solution()
assert sol.minSwapsCouples([0,2,1,3]) == 1
assert sol.minSwapsCouples([0,2,3,4,5,1,6,8,7,9]) == 3
assert sol.minSwapsCouples([5,4,2,6,3,1,0,7]) == 2
