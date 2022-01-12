from typing import List

class Solution:
  """ 
  Old style dp = [[[None for _ in range(C)] for _ in range(C)] for _ in range(R)]
  """
  def cherryPickup(self, grid: List[List[int]]) -> int:
    R, C = len(grid), len(grid[0])
    
    dp = [[[None] * C for _ in range(C)] for _ in range(R)]
    hasCache = [[[False] * C for _ in range(C)] for _ in range(R)]
    def dfs(x, y1, y2):
      if x == R: return 0 # reach the bottom or base case
      if hasCache[x][y1][y2]: return dp[x][y1][y2]
      
      score = 0
      if y1 == y2: # handle collision
        score += grid[x][y1]
      else:
        score += grid[x][y1] + grid[x][y2]
      
      best = 0
      for dy1 in range(-1, 2):
        ny1 = y1 + dy1
        if 0 <= ny1 < C:
          for dy2 in range(-1, 2):
            ny2 = y2 + dy2
            if 0 <= ny2 < C:
              best = max(best, dfs(x + 1, ny1, ny2))
      hasCache[x][y1][y2] = True
      dp[x][y1][y2] = best + score
      return dp[x][y1][y2]
    ans = dfs(0, 0, C - 1)
    # print(f'{dp}')
    # print(f'{ans}')
    return ans
    
  def cherryPickup_myIdea_notSolve(self, grid: List[List[int]]) -> int:
    DIR = [[-1,1],[-1,0],[-1,-1]]
    R, C = len(grid), len(grid[0])
    dp = [[0 for _ in range(C)] for _ in range(R + 1)]
    def isValid(x, y):
      return x >= 0 and x < R and y >= 0 and y < C
    def dfs(pos):
      x, y = pos
      for deltaX, deltaY in DIR:
        newX, newY = x + deltaX, y + deltaY
        if isValid(newX, newY):
          newVal = dp[x][y] + grid[newX][newY]
          dp[newX][newY] = max(dp[newX][newY], newVal)
          dfs([newX, newY])
    for i in range(C):
      dfs([R, i])
    print(f'{dp}')

sol = Solution()
assert sol.cherryPickup([[3,1,1],[2,5,1],[1,5,5]]) == 21
assert sol.cherryPickup([[3,1,1],[2,5,1],[1,5,5],[2,1,1]]) == 24

"""Debugging

input [[3,1,1],[2,5,1],[1,5,5]]
[
  Row 0 -> [[None, None, 21], [None, None, None], [None, None, None]], 
  Row 1 -> [[None, 17, 13], [None, 15, 16], [None, None, None]], 
  Row 2 -> [[1, 6, 6], [6, 5, 10], [6, 10, 5]]
]
"""
