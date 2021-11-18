from typing import List

class Solution:
  def numTeams(self, rating: List[int]) -> int:
    res = 0
    for i in range(len(rating)):
      lesserLeft = 0
      greaterRight = 0
      greaterLeft = 0
      lesserRight = 0
      for j in range(len(rating)):
        if j < i :
          if rating[j] < rating[i]:
            lesserLeft += 1
          elif rating[j] > rating[i]: 
            greaterLeft += 1
        else:
          if rating[j] < rating[i]:
            lesserRight += 1
          elif rating[j] > rating[i]: 
            greaterRight += 1
      res += greaterLeft * lesserRight
      res += lesserLeft * greaterRight
    return res  
        
sol = Solution()
assert sol.numTeams([2,5,3,4,1]) == 3
assert sol.numTeams([2,1,3]) == 0
assert sol.numTeams([1,2,3,4]) == 4
