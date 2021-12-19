from typing import List

class Solution:
  def rob(self, nums: List[int]) -> int:
    if len(nums) < 3:
      return max(nums)
    def robSegment(nums):
      if len(nums) == 0:
        return 0
      if len(nums) < 3:
        return max(nums)
      dpArr = [0 for _ in range(len(nums))]
      dpArr[0] = nums[0]
      dpArr[1] = max(nums[0], nums[1])
      for i in range(2, len(nums)):
        dpArr[i] = max(nums[i] + dpArr[i - 2], dpArr[i - 1])
      # print(f'{dpArr[len(nums) - 1]}')
      return dpArr[len(nums) - 1]
    ans_notIncludeFirst = robSegment(nums[1:])
    ans_includeFirst = nums[0] + robSegment(nums[2:len(nums) - 1])
    # print(f'{max(ans_includeFirst, ans_notIncludeFirst)}')
    return max(ans_includeFirst, ans_notIncludeFirst)
 
  def rob_notSoGood(self, nums: List[int]) -> int:
    '''
    Not good because there are two space complexity is O(2n)
    '''
    def robSegment(nums, curIndex, dp):
      if curIndex >= len(nums):
        return 0
      if not curIndex in dp:
        ans = max(nums[curIndex] + robSegment(nums, curIndex + 2, dp), robSegment(nums, curIndex + 1, dp))
        dp[curIndex] = ans
      return dp[curIndex]
    # dp = {}
    ans_notIncludeFirst = robSegment(nums, 1, {})
    # dp[len(nums) - 2] = 0
    ans_includeFirst = nums[0] + robSegment(nums[0:len(nums) - 1], 2, {})
    # print(f'{max(ans_includeFirst, ans_notIncludeFirst)}')
    return max(ans_includeFirst, ans_notIncludeFirst)
sol = Solution()
assert sol.rob([2,3,4]) == 4
assert sol.rob([2,3,2]) == 3
assert sol.rob([2,1,2,5,1]) == 7
assert sol.rob([2,99,3,4]) == 103
assert sol.rob([3,1,3,100]) == 103
assert sol.rob([1,3,1,3,100]) == 103
assert sol.rob([94,40,49,65,21,21,106,80,92,81,679,4,61,6,237,12,72,74,29,95,265,35,47,1,61,397,52,72,37,51,1,81,45,435,7,36,57,86,81,72]) == 2926
