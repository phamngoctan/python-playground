from typing import List

class Solution:
  def findCenter(self, edges: List[List[int]]) -> int:
    return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]
sol = Solution()
assert sol.findCenter([[1,2],[2,3],[4,2]]) == 2
assert sol.findCenter([[1,2],[5,1],[1,3],[1,4]]) == 1
