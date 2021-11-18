from typing import List

class Solution:
  '''
  Sliding window approach
  '''
  def minOperations(self, nums: List[int], x: int) -> int:
    neededSumForSubarray = sum(nums) - x
    if neededSumForSubarray == 0:
      return len(nums)
    curSum, start, res = 0, 0, -1
    for end in range(len(nums)):
      curSum += nums[end]
      while curSum >= neededSumForSubarray and start < len(nums):
        if curSum == neededSumForSubarray:
          res = max(res, end - start + 1)
        curSum -= nums[start]
        start += 1
    if res == -1:
      return res
    # print(f'{len(nums) - res}')
    return len(nums) - res
sol = Solution()
assert sol.minOperations([1,1,4,2,3], x = 5) == 2
assert sol.minOperations([5,6,7,8,9], x = 4) == -1
assert sol.minOperations([3,2,20,1,1,3], x = 10) == 5
assert sol.minOperations([1,1], x = 2) == 2
assert sol.minOperations([1,1,4], x = 6) == 3
assert sol.minOperations([8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309], x = 134365) == 16
assert sol.minOperations([1,1], x = 3) == -1
