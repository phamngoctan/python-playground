class Solution:

  # def knightProbabilityBottomUp with optimisation, two dp only
  def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
    directions = [[-2,-1],[-1,-2],[1,-2],[2,-1],[2,1],[1,2],[-1,2],[-2,1]]
    def isValid(x, y):
      return x >= 0 and x < n and y >= 0 and y < n

    prevDP = [[0 for i in range(n)] for j in range(n)]
    curDP = [[0 for i in range(n)] for j in range(n)]
    prevDP[row][column] = 1
    # print(f'{dp}')
    for step in range(1, k + 1):
      for r in range(n):
        for c in range(n):
          for dirX, dirY in directions:
            previousX = r + dirX
            previousY = c + dirY
            if isValid(previousX, previousY):
              curDP[r][c] += prevDP[previousX][previousY]/8
      prevDP = curDP
      curDP = [[0 for i in range(n)] for j in range(n)]
    res = 0
    for i in range(n):
      for j in range(n):
        res += prevDP[i][j]
    # print(f'{res}')
    return res
  
  def knightProbabilityBottomUp(self, n: int, k: int, row: int, column: int) -> float:
    directions = [[-2,-1],[-1,-2],[1,-2],[2,-1],[2,1],[1,2],[-1,2],[-2,1]]
    def isValid(x, y):
      return x >= 0 and x < n and y >= 0 and y < n

    dp = [[[0 for i in range(n)] for j in range(n)] for step in range(k + 1)]
    dp[0][row][column] = 1
    # print(f'{dp}')
    for step in range(1, k + 1):
      for r in range(n):
        for c in range(n):
          for dirX, dirY in directions:
            previousX = r + dirX
            previousY = c + dirY
            if isValid(previousX, previousY):
              dp[step][r][c] += dp[step - 1][previousX][previousY]/8
    # print(f'{dp}')
    # print(f'=========================')
    # print(f'{dp[k]}')
    res = 0
    for i in range(n):
      for j in range(n):
        res += dp[k][i][j]
    # print(f'{res}')
    return res

  def knightProbabilityTopDown(self, n: int, k: int, row: int, column: int) -> float:
    directions = [[-2,-1],[-1,-2],[1,-2],[2,-1],[2,1],[1,2],[-1,2],[-2,1]]
    def isNotValid(x, y):
      return x < 0 or x >= n or y < 0 or y >= n
    def helper(x, y, k, dp):
      if k == 0:
        return 1
      totalProb = 0
      if (k,x,y) in dp:
        return dp[(k,x,y)]
      for deltaX, deltaY in directions:
        newX = x + deltaX
        newY = y + deltaY
        if isNotValid(newX, newY):
          continue
        totalProb += helper(newX, newY, k - 1, dp)
      res = totalProb/8
      dp[(k,x,y)] = res
      return res
    dp = {}
    res = helper(row, column, k, dp)
    # print(f'{res}')
    return res

sol = Solution()
assert sol.knightProbability(n = 6, k = 2, row = 2, column = 2) == 0.53125
assert sol.knightProbability(n = 3, k = 1, row = 0, column = 0) == 0.25
assert sol.knightProbability(n = 3, k = 2, row = 0, column = 0) == 0.06250
assert sol.knightProbability(n = 6, k = 1, row = 2, column = 2) == 1
assert sol.knightProbability(n = 1, k = 0, row = 0, column = 0) == 1
# assert sol.knightProbability(n = 8, k = 30, row = 6, column = 4) == 0.0001905256629833365 # TLE without using dp
assert sol.knightProbability(n = 8, k = 30, row = 6, column = 4) == 0.00019052566298333648 # TLE without using dp
