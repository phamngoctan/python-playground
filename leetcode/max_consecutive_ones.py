from typing import List

class Solution:
  def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    left = -1
    ans = -2
    for i in range(len(nums)):
      if nums[i] == 0:
        left = i
      else:
        ans = max(ans, i - left)
    return 0 if ans == -2 else ans
