from typing import List

class Solution:
  def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    fre = {}
    for i, v in enumerate(nums):
      if v in fre and i - fre[v] <= k:
        return True
      fre[v] = i
    return False
  
  def containsNearbyDuplicateSlow(self, nums: List[int], k: int) -> bool:
    fre = {}
    for i in range(len(nums)):
      if nums[i] in fre and i - fre[nums[i]] > k:
        return True
      else:
        fre[nums[i]] = i
    return False

sol = Solution()
assert sol.containsNearbyDuplicate([1,2,3,1], 3) == True
assert sol.containsNearbyDuplicate([1,0,1,1], 1) == True
assert sol.containsNearbyDuplicate([1,2,3,1,2,3], 2) == False
assert sol.containsNearbyDuplicate([1], 0) == False
