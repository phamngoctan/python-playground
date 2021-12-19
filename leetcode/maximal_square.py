from typing import List

class Solution:
  def maximalSquare(self, matrix: List[List[str]]) -> int:
    '''
    in Python, the -1 position turns to the last position in array,
    so don't need to do something additionally compare to Java
    '''
    R, C = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(C + 1)] for _ in range(R + 1)]
    maxSize = 0
    for i in range(R):
      for j in range(C):
        if matrix[i][j] == '1':
          dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
          maxSize = max(maxSize, dp[i][j])
    return maxSize * maxSize
  
  def maximalSquare_myThinking(self, matrix: List[List[str]]) -> int:
    R, C = len(matrix), len(matrix[0])
    def isValid(x, y):
      return x >= 0 and x < R and y >= 0 and y < C
    dp = [[0 for _ in range(C)] for _ in range(R)]
    maxSize = 0
    for i in range(R):
      for j in range(C):
        if matrix[i][j] == '1':
          crossLeft = int(dp[i - 1][j - 1]) if isValid(i - 1, j - 1) else 0
          left = int(dp[i - 1][j]) if isValid(i - 1, j) else 0
          above = int(dp[i][j - 1]) if isValid(i, j - 1) else 0
          dp[i][j] = min(crossLeft, left, above) + 1
          maxSize = max(maxSize, dp[i][j])
    # print(f'{dp}')
    return maxSize * maxSize
sol = Solution()
assert sol.maximalSquare([["1","1","1","1","0"],
                          ["1","1","1","1","0"],
                          ["1","1","1","1","1"],
                          ["1","1","1","1","1"],
                          ["0","0","1","1","1"]]) == 16
assert sol.maximalSquare([["1","0","1","0","0"],
                          ["1","0","1","1","1"],
                          ["1","1","1","1","1"],
                          ["1","0","0","1","0"]]) == 4
