from typing import List

"""
n/2 + n/4 + n/8 + ... = n
log(n/2) + log(n/4) + log(n/8) + ... = log(n)
Time complexity is 3log(n) => log(n)"""
class Solution:
  def searchRange(self, nums: List[int], target: int) -> List[int]:
    mid = self.binary_search(nums, 0, len(nums) - 1, target)
    if mid == -1:
      return [-1, -1]
    else:
      newLeft = tempL = mid
      while tempL != -1: # perform the search at least once
        newLeft = tempL
        tempL = self.binary_search(nums, 0, newLeft - 1, target)
      newRight = tempR = mid
      
      while tempR != -1:
        newRight = tempR
        tempR = self.binary_search(nums, newRight + 1, len(nums) - 1, target)
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
