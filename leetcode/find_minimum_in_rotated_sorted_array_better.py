from typing import List

class Solution:
  def findMin(self, nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1
    while left < right:
      mid = left + (right-left)//2
      if nums[mid] < nums[right]:
        right = mid
      else:
        left = mid + 1
    return nums[left]

sol = Solution()
assert sol.findMin([3,4,5,1,2]) == 1
assert sol.findMin([4,5,6,7,0,1,2]) == 0
# assert sol.findMin([0,1,2,4,5,6,7]) == 0 # not a valid test case
assert sol.findMin([0]) == 0
assert sol.findMin([1,0]) == 0
assert sol.findMin([1,2,0]) == 0
assert sol.findMin([2,3,4,5,1]) == 1
assert sol.findMin([5,1,2,3,4]) == 1
assert sol.findMin([5,1,2]) == 1
assert sol.findMin([2,5,1]) == 1