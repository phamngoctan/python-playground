from typing import List

class Solution:
  def rob(self, nums: List[int]) -> int:
    '''
    DP With memorization
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
assert sol.rob([1,2,3,1]) == 4
assert sol.rob([2,1,1,3]) == 5
assert sol.rob([2]) == 2
assert sol.rob([2,7,9,3,1]) == 12
