#from typing import List

class Solution:
    def numberOfSteps (self, num: int) -> int:
		if (num == 0):
			return 0
        count = 0
        while (num):
          if (num & 1):
            count += 2
          else:
            count += 1
          num >>= 1
        return count - 1
    
s = Solution()
print(s.numberOfSteps(8))

# 101 odd
#  10 -> divide and minus one -> count as two steps

# 100 even
#  10 -> just divide only -> count as one step

# except the last one, just - 1 only