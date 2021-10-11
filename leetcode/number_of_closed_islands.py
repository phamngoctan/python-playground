from typing import List

class Solution:
  def closedIsland(self, grid: List[List[int]]) -> int:
    R = len(grid)
    C = len(grid[0])
    def valid(x, y):
      return x >= 0 and x < R and y >= 0 and y < C
    direction = [[0,1],[0,-1],[1,0],[-1,0]]
    def dfs(grid, pos):
      x,y = pos
      grid[x][y] = 1
      for dir in direction:
        newX = x + dir[0]
        newY = y + dir[1]
        if not valid(newX, newY) or grid[newX][newY] == 1:
          continue
        dfs(grid, [newX, newY])
    for i in range(R):
      for j in range(C):
        if (i == 0 or i == R - 1 or j == 0 or j == C - 1) and grid[i][j] == 0:
          dfs(grid, [i, j])
    count = 0
    for i in range(R):
      for j in range(C):
        if grid[i][j] == 0:
          dfs(grid, [i, j])
          count += 1
    # print(f'{count}')
    return count
sol = Solution()
assert sol.closedIsland([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]) == 2
assert sol.closedIsland([[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]) == 1
assert sol.closedIsland(
  [[1,1,1,1,1,1,1],
  [1,0,0,0,0,0,1],
  [1,0,1,1,1,0,1],
  [1,0,1,0,1,0,1],
  [1,0,1,1,1,0,1],
  [1,0,0,0,0,0,1],
  [1,1,1,1,1,1,1]]) == 2
