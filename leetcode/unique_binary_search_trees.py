class Solution:
  def numTrees(self, n: int) -> int:
    """
    formula: t(i - 1) * t(n - i) 
    i in range(1, n + 1)
    i.e: t(2)
    i = 2 => t(0) * t(1) + t(1) * t(0)
    i = 3 => t(0)*t(2) + t(1)*t(1) + t(2)*t(0)
    """
    dp = [0 for _ in range(n + 1)]
    def helper(cur, dp):
      if cur == 1 or cur == 0:
        return 1
      if dp[cur] == 0:
        res = 0
        for i in range(1, cur + 1):
          res += helper(i - 1, dp) * helper(cur - i, dp)
        dp[cur] = res
        # print(f'{res}')
      return dp[cur]
    return helper(n, dp)
sol = Solution()
assert sol.numTrees(3) == 5
assert sol.numTrees(2) == 2
assert sol.numTrees(1) == 1
assert sol.numTrees(0) == 1
assert sol.numTrees(4) == 14
assert sol.numTrees(5) == 42