from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    curMax = 0
    maxSoFar = 0
    for i in range(1, len(prices)):
      curMax += prices[i] - prices[i - 1]
      curMax = max(0, curMax) # reset to 0 if curMax is negative. Means consider the new sub array
      maxSoFar = max(maxSoFar, curMax)
    return maxSoFar
sol = Solution()
assert sol.maxProfit([7,1,5,3,6,4]) == 5
assert sol.maxProfit([7,2,5,1,6,4]) == 5
assert sol.maxProfit([1,5,3,6,4,8,6,1,10]) == 9
assert sol.maxProfit([0, 6, -3, 7]) == 10
