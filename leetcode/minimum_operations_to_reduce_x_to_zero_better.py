from typing import List

class Solution:
  '''
  Prefix sum/map approach - finding longest target sub-array
  '''
  def minOperations(self, nums: List[int], x: int) -> int:
    neededSumForSubarray = sum(nums) - x
    if neededSumForSubarray == 0:
      return len(nums)
    prefixHash = {0:-1}
    res = -2
    curSum = 0
    for i in range(len(nums)):
      curSum += nums[i]
      prevSum = curSum - neededSumForSubarray
      if prevSum in prefixHash:
        res = max(res, i - prefixHash[prevSum])
      prefixHash[curSum] = i
    if res == -2:
      return -1
    return len(nums) - res
sol = Solution()
assert sol.minOperations([1,1,4,2,3], x = 5) == 2
assert sol.minOperations([5,6,7,8,9], x = 4) == -1
assert sol.minOperations([3,2,20,1,1,3], x = 10) == 5
assert sol.minOperations([1,1], x = 2) == 2
assert sol.minOperations([1,1,4], x = 6) == 3
assert sol.minOperations([8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309], x = 134365) == 16
