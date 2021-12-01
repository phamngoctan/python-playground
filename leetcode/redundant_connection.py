from typing import List

class Solution:
  def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    parent = [i for i in range(len(edges) + 1)] # nodeId is parent itself
    def findSet(u):
      while u != parent[u]:
        u = parent[u]
      return u
    def unionSet(u, v):
      uParent = findSet(u)
      vParent = findSet(v)
      if uParent == vParent:
        return True
      parent[uParent] = vParent
    for u, v in edges:
      if unionSet(u, v):
        return [u, v]
sol = Solution()
assert sol.findRedundantConnection([[1,2],[1,3],[2,3]]) == [2,3]
assert sol.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]) == [1,4]
assert sol.findRedundantConnection([[1,2],[2,1]]) == [2,1]
