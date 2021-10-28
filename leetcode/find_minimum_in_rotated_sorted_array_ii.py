from typing import List

class Solution:
  def findMin(self, nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1
    while left < right:
      mid = left + (right - left) // 2
      if nums[mid] < nums[right]:
        right = mid
      elif nums[mid] > nums[right]:
        left = mid + 1
      else:
        if nums[right - 1] > nums[right]: # optimization
          left = right;
          break;
        right -= 1
    # print(f'{left}')
    return nums[left]
sol = Solution()
assert sol.findMin([3,3,3,1,3]) == 1
assert sol.findMin([3,1,3,3,3]) == 1
assert sol.findMin([3,3,1,3]) == 1
assert sol.findMin([3,3,1,2,3]) == 1
assert sol.findMin([1,3,3,3,3,3,3,3,3]) == 1
assert sol.findMin([1,3,3]) == 1
assert sol.findMin([1,3,5]) == 1
assert sol.findMin([2,2,2,0,1]) == 0
assert sol.findMin([1,2,1,1,1]) == 1
assert sol.findMin([1,1,1,1,1,1,1,1,2,1,1]) == 1
assert sol.findMin([1,1,1,1,1,2,1,1,1,1,1]) == 1
