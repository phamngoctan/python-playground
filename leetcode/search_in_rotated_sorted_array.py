from typing import List

class Solution:
  '''
  Input nums has no duplicated elements
  Time complexity is log(n)
  '''
  def search(self, nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left < right:
      mid = left + (right - left)//2
      if nums[mid] == target: 
        return mid
      if nums[mid] < nums[right]:
        if nums[mid] < target <= nums[right]:
          left = mid + 1
        else:
          right = mid - 1
      else:
        if nums[left] <= target < nums[mid]:
          right = mid - 1
        else:
          left = mid + 1
    if nums[left] == target:
      return left
    return -1

sol = Solution()
assert sol.search([4,5,6,7,0,1,2], target = 0) == 4
assert sol.search([8,1,2,4,5,6,7], target = 0) == -1
assert sol.search([9,10,1,2,4,5,8], target = 9) == 0
assert sol.search([5,8,9,10,1,2,4], target = 2) == 5
