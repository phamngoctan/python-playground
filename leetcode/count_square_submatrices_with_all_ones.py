from typing import List

class Solution:
  '''
  Develop the idea from problem LC 221 maximal-square
  '''
  def countSquares(self, matrix: List[List[int]]) -> int:
      R, C = len(matrix), len(matrix[0])
      dp = [[0 for _ in range(C + 1)] for _ in range(R + 1)]
      ans = 0
      for i in range(R):
          for j in range(C):
              if matrix[i][j] == 1:
                  dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                  ans += dp[i][j]
      # print(f'{dp}')
      return ans