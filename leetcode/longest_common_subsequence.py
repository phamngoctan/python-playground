class Solution:
  def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    R, C = len(text1), len(text2)
    dp = [[0 for _ in range(C + 1)] for _ in range(R + 1)]
    for i in range(R):
      for j in range(C):
        if text1[i] == text2[j]:
          dp[i][j] = dp[i-1][j-1] + 1
        else:
          dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    # print(f'{dp} {R} {C}  {dp[R][C]}')
    return dp[R - 1][C - 1]
sol = Solution()
assert sol.longestCommonSubsequence("abcde", text2 = "ace") == 3
assert sol.longestCommonSubsequence("abc", text2 = "abc") == 3
assert sol.longestCommonSubsequence("abc", text2 = "def") == 0
