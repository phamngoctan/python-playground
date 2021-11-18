from typing import List

class Solution:
  def firstMissingPositive(self, nums: List[int]) -> int:
    # since hashing key must starts from 0
    # need to append 0, in case [1,2,3,4]
    # if we won't add, we can't manipulate 0th index
    # as hash function won't reach there
    nums.append(0)
    n = len(nums)
    for i in range(len(nums)): #delete those useless elements
      if nums[i]<0 or nums[i]>=n:
        nums[i]=0
    for i in range(len(nums)): #use the index as the hash to record the frequency of each number
      nums[nums[i] % n] += n
    # [1,3,4,-1,-2] -> [19,9,4,6,6]
    for i in range(1,len(nums)): # first i that smaller than n is the first missing positive
      if nums[i] // n == 0:
        return i
    return n
    
sol = Solution()
assert sol.firstMissingPositive([1,3,4,-1,-2]) == 2
assert sol.firstMissingPositive([1,2,0]) == 3
assert sol.firstMissingPositive([3,4,-1,1]) == 2
assert sol.firstMissingPositive([7,8,9,11,12]) == 1
