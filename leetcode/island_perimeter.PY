from typing import List

class Solution:
  def islandPerimeter(self, grid: List[List[int]]) -> int:
    if len(grid) == 0:
      return 0
    
    global perimeter
    perimeter = 0
    direction = [[0,-1],[0,1],[1,0],[-1,0]]
    R = len(grid)
    C = len(grid[0])
    
    def dfs(grid, pos):
      if grid[pos[0]][pos[1]] == 0:
        return
      global perimeter
      grid[pos[0]][pos[1]] = 2
      curPerimeter = 4
      toBeMoved = []
      for i in range(4):
        newX = pos[0] + direction[i][0]
        newY = pos[1] + direction[i][1]
        if isInvalid(newX, newY) or grid[newX][newY] == 0:
          continue
        if grid[pos[0]][pos[1]] == 2:
          curPerimeter -= 1
        else:
          toBeMoved.append([newX, newY])        
      
      perimeter += curPerimeter
      for i in range(len(toBeMoved)):
        dfs(grid, toBeMoved[i])

    def isInvalid(x, y):
      return x< 0 or x > R-1 or y<0 or y>C-1 
    
    for i in range(len(grid)):
      for j in range(len(grid[i])):
        dfs(grid, [i,j])
    # print(f'{perimeter}')
    return perimeter

sol = Solution()
assert sol.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]) == 16
assert sol.islandPerimeter([[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,1]]) == 8
assert sol.islandPerimeter([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]) == 0
assert sol.islandPerimeter([[1,1,0,0],[1,1,0,0],[0,0,0,0],[0,0,0,0]]) == 8