from typing import List
import sys

class Solution:
  def deleteAndEarn(self, nums: List[int]) -> int:
    MAX_VALUE = 10**4 + 1
    points = [0 for _ in range(MAX_VALUE)]
    for val in nums:
      points[val] += val
    dp = [0 for _ in range(MAX_VALUE)]
    dp[0] = points[0]
    dp[1] = points[1]
    for i in range(2, MAX_VALUE):
      dp[i] = max(points[i] + dp[i - 2], dp[i - 1])
    return dp[MAX_VALUE - 1]
    
  def deleteAndEarn__topDownArray(self, nums: List[int]) -> int:
    MAX_VALUE = 10**4 + 1
    points = [0 for _ in range(MAX_VALUE)]
    for val in nums:
      points[val] += val
    take, skip = 0, 0
    for i in range(MAX_VALUE):
      takeI = skip + points[i]
      skipI = max(skip, take)
      take = takeI
      skip = skipI
    return max(take, skip)
      
  def deleteAndEarn__topDownRecursion(self, nums: List[int]) -> int:
    '''Using recursion to solve
    '''
    MAX_VALUE = 10**4 + 1
    sys.setrecursionlimit(MAX_VALUE)
    points = [0 for _ in range(MAX_VALUE)]
    for val in nums:
      points[val] += val
    def solve(index, dp):
      if index >= MAX_VALUE:
        return 0
      if not index in dp:
        curVal = points[index] + solve(index + 2, dp)
        dp[index] = max(curVal, solve(index + 1, dp))
      return dp[index]
    dp = {}
    ans = solve(0, dp)
    # print(f'{dp}')
    # print(f'{ans}')
    return ans
  
  def deleteAndEarn_wrongVersion(self, nums: List[int]) -> int:
    '''Wrong approach when using the nums by keySet, 
    Should use the array from 0 -> 10**4 + 1 instead
    '''
    nums.sort()
    countByItem = {}
    for val in nums:
      if not val in countByItem:
        countByItem[val] = 0
      countByItem[val] += 1
    # print(f'{countByItem}')
    nums = sorted(list(countByItem.keys()))
    # print(f'{nums}')
    N = len(nums)
    
    self.ans = float('-inf')
    def solve(index, dp):
      if index >= N:
        return 0
      if not index in dp:
        curVal = nums[index] * countByItem[nums[index]] + solve(index + 2, dp)
        dp[index] = max(curVal, solve(index + 1, dp))
      return dp[index]
    dp = {}
    self.ans = solve(0, dp)
    print(f'{dp}')
    # print(f'--------------')
    return self.ans

sol =  Solution()
assert sol.deleteAndEarn([2,3,4,10,300]) == 316
assert sol.deleteAndEarn([3,4,2]) == 6
assert sol.deleteAndEarn([2,2,3,3,3,4]) == 9
assert sol.deleteAndEarn([2,2,3,3,3,4,2,2,3,3,3,4,2,2,3,3,3,4,2,2,3,3,3,4,2,2,3,3,3,4,2,2,3,3,3,4,2,2,3,3,3,4,2,2,3,3,3,4,2,2,3,3,3,4,2,2,3,3,3,4,2,2,3,3,3,4,2,2,3,3,3,4,2,2,3,3,3,4,2,2,3,3,3,4,2,2,3,3,3,4,2,2,3,3,3,4,2,2,3,3,3,4,2,2,3,3,3,4,2,2,3,3,3,4,2,2,3,3,3,4,2,2,3,3,3,4,2,2,3,3,3,4,2,2,3,3,3,4,2,2,3,3,3,4,2,2,3,3,3,4,2,2,3,3,3,4,2,2,3,3,3,4,5,6,3,19,20,7,1,300,1,2,3,4,10,9,8,54,3,1]) == 653
