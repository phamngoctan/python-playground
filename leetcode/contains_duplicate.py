from typing import List

class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    fre = set()
    for i in range(len(nums)):
      if nums[i] in fre:
        return True
      fre.add(nums[i])
    return False

sol = Solution()
assert sol.containsDuplicate([1,2,3,1]) == True
assert sol.containsDuplicate([1,2,3,4]) == False
assert sol.containsDuplicate([1]) == False