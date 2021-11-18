from typing import List

class Solution:
  def findDuplicate(self, nums: List[int]) -> int:
    # phase 1, finding the first intersection point of two runners
    tortoise = hare = nums[0]
    while True:
      tortoise = nums[tortoise]
      hare = nums[nums[hare]]
      if tortoise == hare:
        break
    
    # phase 2, find the cycle entrance
    tortoise = nums[0]
    while tortoise != hare:
      tortoise = nums[tortoise]
      hare = nums[hare]
    return hare
sol = Solution()
assert sol.findDuplicate([1,3,4,2,2]) == 2
assert sol.findDuplicate([3,1,3,4,2]) == 3
assert sol.findDuplicate([1,1]) == 1
assert sol.findDuplicate([1,1]) == 1
assert sol.findDuplicate([2,2,2,2,2]) == 2
