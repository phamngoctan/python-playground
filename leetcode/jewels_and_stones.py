#from typing import List

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
      my_dict = {}
      lJ = list(J)
      lS = list(S)
      for i in lJ:
        my_dict[i] = 0
      
      for i in lS:
        if (i in my_dict):
          my_dict[i] = my_dict.get(i) + 1
      
      return sum(my_dict.values())

      
    
s = Solution()
print(s.numJewelsInStones("aA", "aAAbbbb"))
