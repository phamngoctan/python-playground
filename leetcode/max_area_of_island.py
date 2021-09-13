from typing import List

class Solution:
  def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    if len(grid) == 0:
      return 0
    direction = [[0,1],[0,-1],[1,0],[-1,0]]
    R = len(grid)
    C = len(grid[0])
    def isNotValid(x, y):
      return x < 0 or y < 0 or x >= R or y >= C
    
    
    def dfs(grid, pos):
      grid[pos[0]][pos[1]] = 0
      total = 0
      for i in range(4):
        newX = pos[0] + direction[i][0]
        newY = pos[1] + direction[i][1]
        if isNotValid(newX, newY) or grid[newX][newY] == 0:
          continue
        total += dfs(grid, [newX, newY])
      return total + 1
      
    maxArea = 0
    for i in range(R):
      for j in range(C):
        if grid[i][j] == 1:
          area = dfs(grid, [i, j])
          # print(f'area at [{i},{j}]: {area}')
          maxArea = max(area, maxArea)
    return maxArea

sol = Solution()
assert sol.maxAreaOfIsland([
  [0,0,1,0,0,0,0,1,0,0,0,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,1,1,0,1,0,0,0,0,0,0,0,0],
  [0,1,0,0,1,1,0,0,1,0,1,0,0],
  [0,1,0,0,1,1,0,0,1,1,1,0,0],
  [0,0,0,0,0,0,0,0,0,0,1,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,0,0,0,0,0,0,1,1,0,0,0,0]]) == 6

assert sol.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]) == 0
assert sol.maxAreaOfIsland([[1]]) == 1
assert sol.maxAreaOfIsland([[1,0],[0,1]]) == 1
assert sol.maxAreaOfIsland([[1,0],[1,1]]) == 3