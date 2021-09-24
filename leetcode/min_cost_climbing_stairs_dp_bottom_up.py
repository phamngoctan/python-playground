from typing import List

class Solution:
  # def minCostClimbingStairs(self, cost: List[int]) -> int:
  #   dp = [0 for i in range(len(cost))]
  #   for i in range(len(cost)):
  #     if i < 2:
  #       dp[i] = cost[i]
  #     else:
  #       dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
  #   return min(dp[len(cost) - 1], dp[len(cost) - 2])

  def minCostClimbingStairs(self, cost: List[int]) -> int:
    for i in range(len(cost)):
      if i >= 2:
        cost[i] = min(cost[i - 1], cost[i - 2]) + cost[i]
    return min(cost[len(cost) - 1], cost[len(cost) - 2])


sol = Solution()
assert sol.minCostClimbingStairs([10,15,20]) == 15
assert sol.minCostClimbingStairs([10,15,30,5]) == 20
assert sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]) == 6