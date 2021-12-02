from typing import Dict, List

class Solution:
  def countServers(self, grid: List[List[int]]) -> int:
    R, C = len(grid), len(grid[0])
    def DFS(grid, pos):
      curX, curY = pos
      grid[curX][curY] = 0 # visited
      totalNodes = 1
      for i in range(R):
        newX, newY = i, curY
        if grid[newX][newY] == 1:
          totalNodes += DFS(grid, [newX, newY])
      for i in range(C):
        newX, newY = curX, i
        if grid[newX][newY] == 1:
          totalNodes += DFS(grid, [newX, newY])
      return totalNodes
    ans = 0
    for i in range(R):
      for j in range(C):
        if grid[i][j] == 1:
          numberOfNodes = DFS(grid, [i,j])
          ans += numberOfNodes if numberOfNodes > 1 else 0
    return ans
          
sol = Solution()
assert sol.countServers([[1,0],[0,1]]) == 0
assert sol.countServers([[1,0],[1,1]]) == 3
assert sol.countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]) == 4
assert sol.countServers([[1,1,0,0],[1,0,1,0],[1,0,1,0],[0,0,0,1]]) == 6
assert sol.countServers(
  [[1,0,0,1,0],
   [0,0,0,0,0],
   [0,0,0,1,0]]) == 3
