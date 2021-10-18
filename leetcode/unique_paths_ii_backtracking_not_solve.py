from typing import List

class Solution:
  def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    R = len(obstacleGrid)
    C = len(obstacleGrid[0])
    if obstacleGrid[R - 1][C - 1] == 1 or obstacleGrid[0][0] == 1:
      return 0
    if R - 1 == 0 and C - 1 == 0:
      return 1
    DIRECTIONS = [[0,1],[1,0]]
    def isValid(x, y):
      return x >= 0 and x < R and y >= 0 and y < C
    def solveBacktrack(obstacleGrid, res, x, y):
      for dir in DIRECTIONS:
        newX = x + dir[0]
        newY = y + dir[1]
        if isValid(newX, newY):
          if newX == R - 1 and newY == C - 1:
            res[0] += 1
          elif obstacleGrid[newX][newY] == 0:
            obstacleGrid[newX][newY] = 1
            solveBacktrack(obstacleGrid, res, newX, newY)
            obstacleGrid[newX][newY] = 0
    res = [0]
    solveBacktrack(obstacleGrid, res, 0, 0)
    # print(f'{res}')
    return res[0]
          
    
sol = Solution()
assert sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]) == 2
assert sol.uniquePathsWithObstacles([[0,1],[0,0]]) == 1
assert sol.uniquePathsWithObstacles([[0,1],[1,0]]) == 0
assert sol.uniquePathsWithObstacles([[0,0,0],[0,0,0],[0,0,0]]) == 6
assert sol.uniquePathsWithObstacles([[0,0],[0,1]]) == 0
