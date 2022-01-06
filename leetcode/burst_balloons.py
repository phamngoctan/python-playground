from typing import List

class Solution:
  def maxCoins(self, nums: List[int]) -> int:
    if len(nums) > 1 and len(set(nums)) == 1:
      # Edge case: all elements in the list are the same number
      return (nums[0] ** 3) * (len(nums) - 2) + nums[0] ** 2 + nums[0]
    
    nums = [1] + nums + [1]
    dp = {} # up to n^2 space complexity, can also use the dp[N][N] to store
    def dfs(left, right):
      if left > right: return 0
      if (left, right) in dp:
        return dp[(left, right)]
      dp[(left, right)] = 0
      for i in range(left, right + 1):
        coins = nums[left - 1] * nums[i] * nums[right + 1]
        coins += dfs(left, i - 1) + dfs (i + 1, right)
        dp[(left, right)] = max(dp[(left, right)], coins)
      return dp[(left, right)]
    ans = dfs(1, len(nums) - 2)
    # print(f'{ans}')
    return ans
         
  def maxCoins_notUnderstand(self, A):
    A, N = [1] + A + [1], len(A) + 2
    dp = [[0] * N for _ in range(N)]
    for i in range(N - 2, -1, -1):
      for j in range(i + 2, N):
        # dp[i][j] = max(A[i]*A[k]*A[j] + dp[i][k] + dp[k][j] for k in range(i + 1, j))
        maxCur = 0
        for k in range(i + 1, j):
          maxCur = max(maxCur, A[i]*A[k]*A[j] + dp[i][k] + dp[k][j])
        dp[i][j] = maxCur
    return dp[0][N-1]
  
  def maxCoins_notSolvedYet(self, nums: List[int]) -> int:
    '''
    BruceForce - but it doesn't solve the problem.
    Time complexity: N!
    '''
    if len(nums) == 1:
      return nums[0]
    if len(nums) == 2:
      i = 0 if nums[0] < nums[1] else 1
      return nums[0] * nums[1] + self.maxCoins(nums[:i] + nums[i + 1:])
    if len(nums) == 3:
      i = 1
      return nums[0] * nums[1] * nums[2] + self.maxCoins(nums[:i] + nums[i + 1:])
    minVal = min(nums)
    ans = 0
    for i in range(len(nums)):
      if nums[i] == minVal:
        leftVal = nums[i - 1] if i > 0 else 1
        rightVal = nums[i + 1] if i < len(nums) - 1 else 1
        curAns = leftVal * nums[i] * rightVal
        curAns += self.maxCoins(nums[:i] + nums[i + 1:])
        ans = max(curAns, ans)
    print(f'{ans}')
    return ans

sol = Solution()
assert sol.maxCoins([3,1,5,8]) == 167
assert sol.maxCoins([1,5]) == 10
assert sol.maxCoins([2,2,1,1,5]) == 50
assert sol.maxCoins([4,6,1,9,8,8,4,1,6]) == 1776