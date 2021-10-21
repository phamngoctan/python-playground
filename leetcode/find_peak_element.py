from typing import List

class Solution:
  def findPeakElement(self, nums: List[int]) -> int:
    if len(nums) == 1:
      return 0
    left = 0
    right = len(nums) - 1
    while left <= right:
      mid = (right - left) // 2 + left
      # print(f'{mid}')
      # right most position and increase
      if nums[mid] > nums[mid - 1] and mid + 1 > right:
        return mid
      # left most position and decrease
      if nums[mid] > nums[mid + 1] and mid - 1 < 0:
        return mid
      if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
        return mid
      if nums[mid] < nums[mid + 1]:
        left = mid + 1
      else:
        right = mid - 1

sol = Solution()
assert sol.findPeakElement([1,2,3,1]) == 2
assert sol.findPeakElement([1,2,1,3,5,6,4]) == 5
assert sol.findPeakElement([1,2,5,4,3,2,1]) == 2
assert sol.findPeakElement([1,2]) == 1
assert sol.findPeakElement([2,1]) == 0
assert sol.findPeakElement([3,1,2]) == 2
assert sol.findPeakElement([3,1]) == 0
assert sol.findPeakElement([3]) == 0
