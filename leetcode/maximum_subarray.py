from typing import List

class Solution:
  
  """[After refactoring]
  """
  def maxSubArray(self, nums: List[int]) -> int:
    res = nums[0]
    curMax = nums[0]
    for i in range(1, len(nums)):
      curMax = max(curMax + nums[i], nums[i])
      res = max(res, curMax)
    return res
  
  """[From Kadane algorithm idea to my implementation]
  """
  def maxSubArray_raw(self, nums: List[int]) -> int:
    if len(nums) == 1:
      return nums[0]
    res = -10**4 - 1
    curMax = -10**4 - 1
    for num in nums:
      curMax += num
      curMax = max(curMax, num)
      res = max(res, curMax)
    # print(f'{res}')
    return res

sol = Solution()
assert sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
assert sol.maxSubArray([-2]) == -2
assert sol.maxSubArray([-2,-1]) == -1
assert sol.maxSubArray([-2,1,3]) == 4
assert sol.maxSubArray([0,-1]) == 0
assert sol.maxSubArray([5,4,-1,7,8]) == 23
