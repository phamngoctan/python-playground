from typing import List

class Solution:
  def findDuplicates(self, nums: List[int]) -> List[int]:
    res = []
    for i in range(len(nums)):
      if nums[abs(nums[i]) - 1] < 0:
        res.append(abs(nums[i]))
      else:
        nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]
    # print(f'{res}')
    return res
sol = Solution()
assert sol.findDuplicates([4,3,2,7,8,2,3,1]) == [2,3]
assert sol.findDuplicates([1,1,2]) == [1]
assert sol.findDuplicates([1,2,2]) == [2]
assert sol.findDuplicates([1]) == []
assert sol.findDuplicates([2,2]) == [2]
assert sol.findDuplicates([1,2,3]) == []
