from typing import List

class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    res = nums[0]
    for i in range(1, len(nums)):
      res = nums[i] ^ res
    return res
sol = Solution()
# print(f'{4 ^ 4 ^ 3}')
assert sol.singleNumber([2,2,1]) == 1
assert sol.singleNumber([4,1,2,1,2]) == 4
assert sol.singleNumber([2]) == 2
