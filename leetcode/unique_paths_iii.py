from typing import List

class Solution: 
  def uniquePathsIII(self, grid: List[List[int]]) -> int:
    R = len(grid)
    C = len(grid[0])
    DIRECTIONS = [[0,1],[0,-1],[1,0],[-1,0]]
    def isValid(r, c):
      return r >= 0 and r < R and c >= 0 and c < C
    def solveBacktrack(grid, res, totalNonObstacle, curStep, r, c):
      for dir in DIRECTIONS:
        newX = r + dir[0]
        newY = c + dir[1]
        if isValid(newX, newY):
          if grid[newX][newY] == 0:
            grid[r][c] = 4
            solveBacktrack(grid, res, totalNonObstacle, curStep + 1, newX, newY)
            grid[r][c] = 0
          elif grid[newX][newY] == 2:
            if curStep == totalNonObstacle:
              res[0] += 1

    totalNonObstacle = 0
    for i in range(R):
      for j in range(C):
        if grid[i][j] == 0:
          totalNonObstacle += 1
    res = [0]
    for i in range(R):
      for j in range(C):
        if grid[i][j] == 1:
          solveBacktrack(grid, res, totalNonObstacle, 0, i, j)
    # print(f'{res}')
    return res[0]

sol = Solution()
assert sol.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]) == 2
assert sol.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]]) == 4
assert sol.uniquePathsIII([[0,1],[2,0]]) == 0