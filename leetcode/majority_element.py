from typing import List

class Solution:
  '''
  This will works only and only when the majority element has size > n/2
  '''
  def majorityElement(self, nums: List[int]) -> int:
    major = nums[0]
    count = 1
    for i in range(1, len(nums)):
      if count == 0:
        major = nums[i]
        count = 1
      elif nums[i] == major:
        count += 1
      else:
        count -= 1
    return major
sol = Solution()
assert sol.majorityElement([2,2,1,1,1,2,2]) == 2
assert sol.majorityElement([3,2,3]) == 3
assert sol.majorityElement([1]) == 1
assert sol.majorityElement([1,1]) == 1
assert sol.majorityElement([5,1,5]) == 5
