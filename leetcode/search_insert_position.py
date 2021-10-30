from typing import List

class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left < right:
      mid = left + (right - left) // 2
      if nums[mid] == target:
        return mid
      if nums[mid] < target:
        left = mid + 1
      else:
        right = mid - 1
    # print(f'{left}')
    if target <= nums[left]: # the equal to ensure case left == right == 0
      return left
    return left + 1
sol = Solution()
assert sol.searchInsert([1,3,5,7], target = 6) == 3
assert sol.searchInsert([1,3,5,7], target = 4) == 2
assert sol.searchInsert([1,3,5,6], target = 5) == 2
assert sol.searchInsert([1,3,5,6], target = 2) == 1
assert sol.searchInsert([1,3,5,6], target = 7) == 4
assert sol.searchInsert([1,3,5,6], target = 0) == 0
assert sol.searchInsert([1], target = 0) == 0
assert sol.searchInsert([1], target = 1) == 0
