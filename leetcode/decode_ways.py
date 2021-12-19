class Solution:
  def numDecodings(self, s: str) -> int:
    dp = {}
    dp[len(s)] = 1
    for i in range(len(s) - 1, -1, -1):
      if s[i] != '0':
        dp[i] = dp[i + 1]
        # consider case two number
        if i < len(s) - 1 and (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
          dp[i] += dp[i + 2]
      else:
        dp[i] = 0
    # print(f'{dp}')
    return dp[0]
        
  
  def numDecodings_recursionWithMemorization(self, s: str) -> int:
    '''
    Main idea: each path is an answer to the result
    10111 -> only go into 10 root, the '0' will not allow any decoding way
    With memorization technique, the time complexity is O(n)
    '''
    def helper(s, pos, dp):
      if not pos in dp:
        # stop the recursion
        if len(s) == pos: return 1 # '0' string will not enter to this condition :D
        if s[pos] == '0': return 0 # also stop the recursion
        ans = helper(s, pos + 1, dp)
        if pos < len(s) - 1 and (s[pos] == '1' or (s[pos] == '2' and s[pos + 1] < '7')):
          ans += helper(s, pos + 2, dp)
        dp[pos] = ans
      return dp[pos]
    # if len(s) == 0: return 0
    ans = helper(s, 0, {})
    # print(f'{ans}')
    return ans
  
  def numDecodings_withoutMemorization(self, s: str) -> int:
    '''
    10111 -> only go into 10 root, the '0' will not allow any decoding way
    Time complexity is O(2^n)
    '''
    def helper(s, pos):
      # stop the recursion
      if len(s) == pos: return 1 # '0' string will not enter to this condition :D
      if s[pos] == '0': return 0 # also stop the recursion
      ans = helper(s, pos + 1)
      if pos < len(s) - 1 and (s[pos] == '1' or (s[pos] == '2' and s[pos + 1] < '7')):
        ans += helper(s, pos + 2)
      return ans
    
    # if len(s) == 0:
    #   return 0
    ans = helper(s, 0)
    # print(f'{ans}')
    return ans
      
sol = Solution()
assert sol.numDecodings("2011") == 2
assert sol.numDecodings("8011") == 0
assert sol.numDecodings("801") == 0
assert sol.numDecodings("80") == 0
assert sol.numDecodings("12") == 2
assert sol.numDecodings("226") == 3
# assert sol.numDecodings("") == 0
assert sol.numDecodings("0") == 0
assert sol.numDecodings("06") == 0
assert sol.numDecodings("11106") == 2
assert sol.numDecodings("1101111") == 5
