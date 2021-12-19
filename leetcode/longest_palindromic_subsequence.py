class Solution:
  def longestPalindromeSubseq(self, s: str) -> int:
    dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
    for i in range(len(s) - 1, -1, -1):
      dp[i][i] = 1
      for j in range(i + 1, len(s)):
        if s[i] == s[j]:
          dp[i][j] = dp[i+1][j-1] + 2
        else:
          dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    # print(f'{dp}')
    return dp[0][len(s)-1]

  def longestPalindromeSubseq_withMemorization(self, s: str) -> int:
    '''
    Memorization technique
    '''
    def longestPalindromeSubseqSegment(left, right, s, dp):
      if left == right:
        return 1
      if left > right:
        return 0
      if not dp[left][right]:
        if s[left] == s[right]:
          dp[left][right] = 2 + longestPalindromeSubseqSegment(left + 1, right - 1, s, dp)
        else:
          dp[left][right] = max(longestPalindromeSubseqSegment(left + 1, right, s, dp),
                    longestPalindromeSubseqSegment(left, right - 1, s, dp))
      return dp[left][right]
    # def concat(a, b):
    #   return int(f"{a}{b}")
    dp = [[None for _ in range(len(s))] for _ in range(len(s))]
    return longestPalindromeSubseqSegment(0, len(s) - 1, s, dp)
  
  def longestPalindromeSubseq_withoutMemorization(self, s: str) -> int:
    def longestPalindromeSubseqSegment(left, right, s):
      if left == right:
        return 1
      if left > right:
        return 0
      if s[left] == s[right]:
        return 2 + longestPalindromeSubseqSegment(left + 1, right - 1, s)
      else:
        return max(longestPalindromeSubseqSegment(left + 1, right, s),
                   longestPalindromeSubseqSegment(left, right - 1, s))
    return longestPalindromeSubseqSegment(0, len(s) - 1, s)

sol = Solution()
assert sol.longestPalindromeSubseq("bbbab") == 4
assert sol.longestPalindromeSubseq("cbbd") == 2
assert sol.longestPalindromeSubseq("euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew") == 159
