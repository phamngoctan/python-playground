from typing import List

class Solution:
  def missingNumber(self, nums: List[int]) -> int:
    total = sum(nums)
    n = len(nums)
    expectedTotal = (n * (n + 1)) / 2
    return int(expectedTotal - total)

  def missingNumber_bitManipulation(self, nums: List[int]) -> int:
    xorRes = 0
    for i, num in enumerate(nums):
      xorRes = xorRes ^ i ^ num
    return xorRes ^ len(nums)
sol = Solution()
assert sol.missingNumber([3,0,1]) == 2
assert sol.missingNumber([0,1]) == 2
assert sol.missingNumber([9,6,4,2,3,5,7,0,1]) == 8
assert sol.missingNumber([9,6,4,2,3,5,7,8,1]) == 0
assert sol.missingNumber([1]) == 0
assert sol.missingNumber([0]) == 1
