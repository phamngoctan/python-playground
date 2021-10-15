class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
    def helper(m, n, dp):
      if m < 0 or n < 0:
        return 0
      if m == 0 and n == 0:
        return 1
      if dp[m][n] > 0:
        return dp[m][n]
      else:
        dp[m][n] = helper(m - 1, n, dp) + helper(m, n - 1, dp)
        return dp[m][n]

    dp = [[0 for _ in range(n)] for _ in range(m)]
    # print(f'{dp}')
    res = helper(m - 1, n - 1, dp)
    # print(f'{res}')
    return res
sol = Solution()
assert sol.uniquePaths(m = 3, n = 2) == 3
assert sol.uniquePaths(m = 3, n = 7) == 28
assert sol.uniquePaths(m = 7, n = 3) == 28