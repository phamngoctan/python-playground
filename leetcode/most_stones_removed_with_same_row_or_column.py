from typing import List

class Solution:
  def removeStones(self, stones: List[List[int]]) -> int:
    '''
    Time complexity: O(n^2)
    '''
    def DFS(stones, index, point):
      curX, curY = point
      visited[index] = True
      for index, stone in enumerate(stones):
        if visited[index] or (curX != stone[0] and curY != stone[1]):
          continue
        DFS(stones, index, stone)
    visited = [False for _ in range(len(stones))]
    islands = 0
    for index, stone in enumerate(stones):
      if not visited[index]:
        DFS(stones, index, stone)
        islands += 1
    return len(stones) - islands
  
  def removeStones(self, stones: List[List[int]]) -> int:
    '''
    Main idea: We call a connected graph as an island.
    One island must have at least one stone left.
    The maximum stones can be removed = stones number - islands number
    Union find approach
    '''
    parent = {}
    def findSet(u):
      while u != parent.setdefault(u, u):
        u = parent[u]
      return u
    def unionSet(u, v):
      uParent = findSet(u)
      vParent = findSet(v)
      if uParent == vParent:
        return
      parent[uParent] = vParent
    for x,y in stones:
      #(use the bitwise operator, change to minus to represent the column)
      unionSet(x, ~y) # ~y = -y - 1 
    
    # print(f'{parent}')
    res = {findSet(x) for x in parent}
    # print(f'{res}')
    return len(stones) - len(res)
sol = Solution()
assert sol.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]) == 5
assert sol.removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]) == 3
