from typing import List

class Solution:
  ''' Solution idea is the same as hard problem - max profit in job scheduling
    Include passenger or NOT include
    Previous hard problem used top down approach 
    - this problem, I borrow from LC bottom approach
    - time comlexity is O(nlogn)
    '''
  def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
    rides.sort()
    startTimes = [i[0] for i in rides]
    dp = [0 for _ in range(len(rides) + 1)] # plus one because it is our base case
    for i in range(len(rides) - 1, -1, -1):
      start, end, tip = rides[i]
      curEarning = end - start + tip
      iPlus2Position = self.bisect_left(startTimes, end)
      dp[i] = max(dp[i + 1], curEarning + dp[iPlus2Position])
    # print(f'{dp}')
    return dp[0]
  
  def bisect_left(self, nums, target):
    # import bisect
    # return bisect.bisect_left(nums, target)
    lo, hi = 0, len(nums)
    while lo < hi:
      mid = (lo + hi - 1) // 2
      if nums[mid] < target:
        lo = mid + 1
      else:
        hi = mid
    return lo

sol = Solution()
assert sol.maxTaxiEarnings(5, [[2,5,4],[1,5,1]]) == 7
assert sol.maxTaxiEarnings(20, rides = [[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]]) == 20
