from typing import List

class Solution:
  def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
    R, C = len(grid1), len(grid1[0])
    DIRECTION = [[1,0],[0,1],[-1,0],[0,-1]]
    def valid(x, y):
      return x >= 0 and x < R and y >= 0 and y < C
    def DFS(cell):
      curX, curY = cell
      subIsland = grid1[curX][curY] == 1
      grid2[curX][curY] = 0
      for x, y in DIRECTION:
        newX, newY = curX + x, curY + y
        if not valid(newX, newY) or not grid2[newX][newY]:
          continue
        subIsland &= DFS([newX, newY])
      return subIsland
    ans = 0
    for i in range(R):
      for j in range(C):
        if grid2[i][j]:
          ans += 1 if DFS([i,j]) else 0
    return ans
  
sol = Solution()
assert sol.countSubIslands(
  grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], 
  grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]) == 3
assert sol.countSubIslands(
  grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], 
  grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]) == 2