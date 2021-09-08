from leetcode.binary_search.binary_search import binary_search
from typing import List

class Solution:
  def searchRange(self, nums: List[int], target: int) -> List[int]:
    left = 0
    right = len(nums) - 1
    mid = binary_search(nums, 0, right, target)
    if mid == -1:
      return [-1, -1]
    else:
      newLeft = mid
      newRight = mid
      while newLeft - 1 >= left and nums[newLeft - 1] == target:
        newLeft -= 1
      while newRight + 1 <= right and nums[newRight + 1] == target:
        newRight += 1
      return [newLeft, newRight]
    
  def binary_search(self, nums, left, right, target):
    while left <= right:
      mid = (left + right) // 2
      curVal = nums[mid]
      if curVal == target:
        return mid
      elif curVal < target:
        left = mid + 1
      else:
        right = mid - 1
    return -1


sol = Solution()
assert sol.searchRange([5,7,7,8,8,10], 8) == [3,4]
assert sol.searchRange([5,7,7,8,8,10], 6) == [-1,-1]
assert sol.searchRange([1,2,3,4,5], 3) == [2,2]
assert sol.searchRange([], 6) == [-1,-1]
assert sol.searchRange([5,5,5,5,5,5,5,5], 5) == [0,7]
