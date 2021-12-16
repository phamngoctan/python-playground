from typing import List

class Solution:
  def rob(self, nums: List[int]) -> int:
    if len(nums) < 3:
      return max(nums)
    def robSegment(nums):
      if len(nums) < 3:
        return max(nums)
      dpArr = [0 for _ in range(len(nums))]
      dpArr[0] = nums[0]
      dpArr[1] = max(nums[0], nums[1])
      for i in range(2, len(nums)):
        dpArr[i] = max(nums[i] + dpArr[i - 2], dpArr[i - 1])
      return dpArr[len(nums) - 1]
    ans = robSegment(nums)
    # print(f'{ans}')
    return ans
  
  def rob_notSoGood(self, nums: List[int]) -> int:
    '''
    DP With memorization - bottom up approach
    '''
    def robSegment(nums, i, dp: dict):
      if not i in dp:
        if i < 0:
          return 0
        ans = max(nums[i] + robSegment(nums, i - 2, dp), robSegment(nums, i - 1, dp))
        dp[i] = ans
      return dp[i]
    ans = robSegment(nums, len(nums) - 1, {})
    print(f'{ans}')
    return ans
  
  def rob_topDown(self, nums: List[int]) -> int:
    '''
    DP With memorization - top down approach
    '''
    def robSegment(nums, currentIndex, dp: dict):
      if not currentIndex in dp:
        if len(nums) == 1:
          return nums[0]
        if len(nums) == 2:
          return max(nums)
        ans = max(nums[0] + robSegment(nums[2:], currentIndex + 2, dp), robSegment(nums[1:], currentIndex + 1, dp))
        dp[currentIndex] = ans
      return dp[currentIndex]
    ans = robSegment(nums, 0, {})
    # print(f'{ans}')
    return ans
  
  def rob_TLE(self, nums: List[int]) -> int:
    if len(nums) == 1:
      return nums[0]
    if len(nums) == 2:
      return max(nums)
    ans = max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))
    return ans
sol = Solution()
assert sol.rob([3,1,3,100]) == 103
assert sol.rob([1,2,3,1]) == 4
assert sol.rob([2,1,1,3]) == 5
assert sol.rob([2]) == 2
assert sol.rob([2,7,9,3,1]) == 12
