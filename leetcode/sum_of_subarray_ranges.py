from typing import List

class Solution:
  def subArrayRanges(self, nums: List[int]) -> int:
    return self.sumMaxSubArray(nums) - self.sumMinSubArray(nums)
  
  def sumMinSubArray(self, nums) -> int:
    # [3,1,2,4]
    N = len(nums)
    prevLessDist = [i + 1 for i in range(N)] # [1,2,3,4]
    stack = [] # increasing stack (more correctly non-decreasing)
    for index, val in enumerate(nums):
      while stack and stack[-1][0] > val:
        stack.pop()
      if stack:
        prevLessDist[index] = index - stack[-1][1]
      stack.append([val, index])
    # print(f'{prevLessDist}') # [1,2,1,1]
    
    stack.clear() # increasing stack (more correctly non-decreasing)
    nextLessDist = [N - i for i in range(N)]
    for index, val in enumerate(nums):
      while stack and stack[-1][0] > val:
        _, prevIndex = stack.pop()
        nextLessDist[prevIndex] = index - prevIndex
      stack.append([val, index])
    # print(f'{nextLessDist}') # [1,3,2,1]
    
    ans = 0
    for i in range(N):
      ans += nums[i] * prevLessDist[i] * nextLessDist[i]
    # print(f'{ans}') # 17
    return ans
  
  def sumMaxSubArray(self, nums) -> int:
    # [3,1,2,4]
    N = len(nums)
    prevLargerDist = [i + 1 for i in range(N)] # [1,2,3,4]
    stack = [] # decreasing stack (more correctly non-increasing)
    for index, val in enumerate(nums):
      while stack and stack[-1][0] < val:
        stack.pop()
      if stack:
        prevLargerDist[index] = index - stack[-1][1]
      stack.append([val, index])
    # print(f'{prevLargerDist}') # [1,1,2,4]
    
    stack.clear()
    nextLargerDist = [N - i for i in range(N)] # [4,3,2,1]
    for index, val in enumerate(nums):
      while stack and stack[-1][0] < val:
        _, prevIndex = stack.pop()
        nextLargerDist[prevIndex] = index - prevIndex
      stack.append([val, index])
    # print(f'{nextLargerDist}') # [3,1,1,1]
    
    ans = 0
    for i in range(N):
      ans += nums[i] * prevLargerDist[i] * nextLargerDist[i]
    # print(f'{ans}') # 30
    return ans

sol = Solution()
assert sol.subArrayRanges([3,1,2,4]) == 13
assert sol.subArrayRanges([1,2,3]) == 4