from typing import List

class Solution:
  def findUnsortedSubarray(self, nums: List[int]) -> int:
    violateMaxValue = -1
    curMax = nums[0]
    for i, num in enumerate(nums):
      if num < curMax:
        violateMaxValue = i
      else:
        curMax = num
    # print(f'violateMaxValue {violateMaxValue}')
    if violateMaxValue == -1:
      return 0
    violateMinValue = len(nums) - 1
    curMin = nums[len(nums) - 1]
    for i in range(len(nums) - 1, -1, -1):
      if nums[i] <= curMin:
        curMin = nums[i]
      else:
        violateMinValue = i
    # print(f'violateMinValue {violateMinValue}')
    return violateMaxValue - violateMinValue + 1
sol = Solution()
assert sol.findUnsortedSubarray([2,1,3]) == 2
assert sol.findUnsortedSubarray([2,1]) == 2
assert sol.findUnsortedSubarray([1,2]) == 0
assert sol.findUnsortedSubarray([2,6,4,8,10,9,15]) == 5 
assert sol.findUnsortedSubarray([1,5,7,8,2,9,1,100,9]) == 8
assert sol.findUnsortedSubarray([5,7,8,2,9,1,100,9]) == 8
