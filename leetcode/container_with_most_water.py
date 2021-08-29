from typing import List

class Solution:
  def maxArea(self, height: List[int]) -> int:
    if len(height) < 2:
      return 0
    i = 0
    j = len(height) - 1
    maxArea = 0
    while i < j:
      cur = min(height[i], height[j]) * (j - i)
      maxArea = max(maxArea, cur)
      curMinHeight = min(height[i], height[j])
      # if min(height[j - 1], height[i]) > min(height[i + 1], height[j]):
      #   j -= 1
      #   print(f'decrease j to {height[j]}')
      # else:
      #   i += 1
      #   print(f'increase i to {height[i]}')
      # print('----')
      if height[i] <= height[j]:
        i += 1
      else:
        j -= 1
    return maxArea

sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7])) # 49
print(sol.maxArea([4,8,1,2,3,9])) # 32
print(sol.maxArea([4,8,1,2,12,1])) # 24
print(sol.maxArea([1,3,2,5,25,24,5])) # 24