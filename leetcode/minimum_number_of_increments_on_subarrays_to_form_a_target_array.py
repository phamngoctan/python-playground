from typing import List

class Solution:
  def minNumberOperations(self, target: List[int]) -> int:
    """count the number of left edges 
    """
    ans = target[0]
    for i in range(1, len(target)):
      ans += max(0, target[i] - target[i - 1])
    return ans

sol = Solution()
assert sol.minNumberOperations([1,2,3,2,1]) == 3
assert sol.minNumberOperations([3,1,1,2]) == 4