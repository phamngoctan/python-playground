from typing import List

class Solution:
  def findPeakElement(self, nums: List[int]) -> int:
    if len(nums) == 1:
      return 0
    left = 0
    right = len(nums) - 1
    while left < right:
      mid = (right - left) // 2 + left
      if nums[mid] < nums[mid + 1]:
        left = mid + 1
      else:
        right = mid
    return left

sol = Solution()
assert sol.findPeakElement([1,2,3,1]) == 2
assert sol.findPeakElement([1,2,1,3,5,6,4]) == 5
assert sol.findPeakElement([1,2,5,4,3,2,1]) == 2
assert sol.findPeakElement([1,2]) == 1
assert sol.findPeakElement([2,1]) == 0
assert sol.findPeakElement([3,1,2]) == 2
assert sol.findPeakElement([3,1]) == 0
assert sol.findPeakElement([3]) == 0
