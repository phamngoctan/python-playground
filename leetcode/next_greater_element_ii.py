from typing import List

class Solution:
  def nextGreaterElements(self, nums: List[int]) -> List[int]:
    res = [-1] * len(nums)
    monotonicStack = []
    for i in range(len(nums) * 2):
      num = nums[i % len(nums)]
      while len(monotonicStack) and num > nums[monotonicStack[-1]]:
        res[monotonicStack.pop()] = num
      monotonicStack.append(i % len(nums))
    # print(f'{res}')
    return res
sol = Solution()
assert sol.nextGreaterElements([1,2,1]) == [2,-1,2]
assert sol.nextGreaterElements([1,2,3,4,3]) == [2,3,4,-1,4]
assert sol.nextGreaterElements([1,5,3,4,3]) == [5,-1,4,5,5]
assert sol.nextGreaterElements([1,4,5,4,3]) == [4,5,-1,5,4]
assert sol.nextGreaterElements([1,2,2,4,3]) == [2,4,4,-1,4]
assert sol.nextGreaterElements([5,4,3,2,5,6]) == [6,5,5,5,6,-1]
assert sol.nextGreaterElements([5,4,3,2,1]) == [-1,5,5,5,5]
assert sol.nextGreaterElements([1]) == [-1]
assert sol.nextGreaterElements([1,2]) == [2,-1]
assert sol.nextGreaterElements([2,1]) == [-1,2]
