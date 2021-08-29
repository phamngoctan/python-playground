from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    indexMapping  = {}
    for i in range(len(nums)):
      sub = target - nums[i];
      if nums[i] in indexMapping.keys():
        return [indexMapping[nums[i]], i]
      else:
        indexMapping[sub] = i
    return None

sol = Solution()
res = sol.twoSum([2,7,11,15], 9)
print(f'{res}')


