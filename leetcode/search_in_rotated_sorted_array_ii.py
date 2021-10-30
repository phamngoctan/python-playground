from typing import List

class Solution:
  '''
  Input nums has duplicated element
  Time complexity is O(n)
  '''
  def search(self, nums: List[int], target: int) -> bool:
    left = 0
    right = len(nums) - 1
    while left < right:
      mid = left + (right - left) // 2
      if nums[mid] == target:
        return True
      if nums[mid] < nums[right]:
        # right = mid
        if nums[mid] < target <= nums[right]:
          left = mid + 1
        else:
          right = mid - 1
      elif nums[mid] > nums[right]:
        # left = mid + 1
        if nums[left] <= target < nums[mid]:
          right = mid - 1
        else:
          left = mid + 1
      else:
        right -= 1
    return nums[left] == target
sol = Solution()
assert sol.search([2,5,6,0,0,1,2], target = 0) == True
assert sol.search([2,5,6,8,9,2,3], target = 0) == False
assert sol.search([2,5,6,8,0,2,3], target = 0) == True
assert sol.search([3,3,3,1,3], target = 0) == False
assert sol.search([3,1,3,3,3], target = 0) == False
assert sol.search([3,3,3,4,3], target = 3) == True
assert sol.search([3,3,1,3,3], target = 0) == False
assert sol.search([2,5,6,0,0,1,2], target = 3) == False
assert sol.search([3,4,1,3,3,3,3], target = 4) == True
