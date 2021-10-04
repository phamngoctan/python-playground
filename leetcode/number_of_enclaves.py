from typing import List

class Solution:
  def numEnclaves(self, grid: List[List[int]]) -> int:
    R = len(grid)
    C = len(grid[0])
    direction = [[0,1],[0,-1],[1,0],[-1,0]]
    def valid(x, y):
      return x >= 0 and x < R and y >= 0 and y < C
    def isXInBorder(x):
      return x == 0 or x == R - 1
    def isYInBorder(y):
      return y == 0 or y == C - 1
    def dfs(grid, pos):
      x,y = pos
      grid[x][y] = 0
      count = 0
      for dir in direction:
        newX = dir[0] + x
        newY = dir[1] + y
        if not valid(newX, newY) or grid[newX][newY] == 0:
          continue
        count += dfs(grid, [newX, newY])
      return count + 1
    for i in range(R):
      for j in range(C):
        if (isXInBorder(i) or isYInBorder(j)) and grid[i][j] == 1:
          dfs(grid, [i,j])
    res = 0
    # we can use for loop to count the 1 block in the grid, no need to perform the DFS :)
    for i in range(R):
      for j in range(C):
        if grid[i][j] == 1:
          res += dfs(grid, [i,j])
    # print(res)
    return res
sol = Solution()
assert sol.numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]) == 3
assert sol.numEnclaves([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]) == 0
assert sol.numEnclaves([[0,0,0],[0,1,0],[0,0,0]]) == 1
assert sol.numEnclaves([[0],[1],[0]]) == 0
assert sol.numEnclaves([[1]]) == 0
