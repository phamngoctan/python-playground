from typing import List
import bisect
import sys

class Solution:
  def jobScheduling__2(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    sys.setrecursionlimit(2500)
    n = len(startTime)
    jobs = sorted(list(zip(startTime, endTime, profit)))
    # print(f'{jobs}')
    startTime = [jobs[i][0] for i in range(n)]
    def helper2(i, dp):
      if i == n:
        return 0
      if not i in dp:
        ans = helper2(i + 1, dp)
        # j = bisect.bisect_left(startTime, jobs[i][1])
        j = self.binary_search_leftMostForInsert(startTime, i, jobs[i][1])

        ans = max(ans, helper2(j, dp) + jobs[i][2])
        dp[i] = ans
        # print(f'ans at {i} is {dp[i]}')
      return dp[i]
    ans = helper2(0, {}) 
    # print(f'{ans}')
    return ans
  
  def binary_search_leftMostForInsert(self, nums, lo, target):
    # import bisect
    # return bisect.bisect_left(nums, target)
    lo, hi = lo, len(nums)
    while lo < hi:
      mid = (lo + hi - 1) // 2
      if nums[mid] < target:
        lo = mid + 1
      else:
        hi = mid
    return lo
  
  def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    n = len(startTime)
    jobs = sorted(list(zip(startTime, endTime, profit)))    
    def helper(i, dp):
      if i == n:
        return 0
      if not i in dp:
        ans = helper(i + 1, dp)
        for j in range(i + 1, n + 1):
          if j == n or jobs[j][0] >= jobs[i][1]:
            ans = max(ans, helper(j, dp) + jobs[i][2])
            break # found the first job from i to n
                  # this causes the (n^2)
                  # can optimise by using binary search with left most item
        dp[i] = ans
      return dp[i]
    ans = helper(0, {})
    # print(f'{ans}')
    return ans
  
sol = Solution()
assert sol.jobScheduling(startTime = [1,2,3,3,5], endTime = [3,4,5,6,6], profit = [10,50,40,70,20]) == 80
assert sol.jobScheduling(startTime = [1,2,3,3,5], endTime = [3,4,5,6,6], profit = [10,50,40,70,80]) == 130
assert sol.jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [10,50,40,70]) == 80
assert sol.jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]) == 120
assert sol.jobScheduling(startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]) == 150
assert sol.jobScheduling(startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]) == 6
