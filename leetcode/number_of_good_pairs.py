from typing import List
import math

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
      d = {}
      for i in range(len(nums)):
        d[nums[i]] = d.get(nums[i], 0) + 1
      
      res = 0
      for k,v in d.items():
        if (v >= 2):
          res += math.factorial(v)/(math.factorial(v - 2) * 2)
      return int(res)
    
s = Solution()
print(s.numIdenticalPairs([1,2,3,1,1,3]))
print(s.numIdenticalPairs([1,1,1,1]))