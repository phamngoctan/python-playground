from typing import List

class Solution:
  def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    if (sum(gas) - sum(cost) < 0):
      # If sum of gas is less than sum of cost, then there is no way to get through all stations.
      return -1
    
    gas_tank, start_index = 0, 0
    for i in range(len(gas)):
      gas_tank += gas[i] - cost[i]
      
      if gas_tank < 0:
        start_index = i + 1
        gas_tank = 0
    return start_index
  
  def canCompleteCircuit_bruceForce(self, gas: List[int], cost: List[int]) -> int:
    """ Bruce force, Time complexity O(n^2)
    """
    N = len(gas)
    for i in range(N):
      j = 0
      tmp = i
      curCost = gas[i]
      while j < N and curCost >= 0:
        nextStation = (tmp + 1) % N
        if curCost < cost[tmp]:
          break
        if j == N - 1 and curCost >= cost[tmp]:
          return i
        curCost = curCost + gas[nextStation] - cost[tmp]
        tmp = nextStation
        j += 1
    return -1
sol = Solution()
assert sol.canCompleteCircuit([1,2,3,4,5], cost = [3,4,5,1,2]) == 3
assert sol.canCompleteCircuit([2,3,4], cost = [3,4,3]) == -1
