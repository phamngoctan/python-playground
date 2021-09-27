from typing import List

class Solution:
  def minCostClimbingStairs(self, cost: List[int]) -> int:
    INF = -1
    def minCost(position, cost, dp):
      if position < 0:
        return 0
      if position == 0 or position == 1:
        return cost[position]
      if dp[position] != INF:
        return dp[position]
      dp[position] = cost[position] + min(minCost(position - 1, cost, dp), minCost(position - 2, cost, dp))
      return dp[position]
    numberOfStars = len(cost)
    dp = [INF for i in range(numberOfStars)]
    return min(minCost(numberOfStars - 1, cost, dp), minCost(numberOfStars - 2, cost, dp))


sol = Solution()
assert sol.minCostClimbingStairs([10,15,20]) == 15
assert sol.minCostClimbingStairs([10,15,30,5]) == 20
assert sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]) == 6