from typing import List

class Solution:
  def maxArea(self, height: List[int]) -> int:
    
    maxArea = 0
    for i in range(len(height)):
      for j in range((i+1), len(height)):
        print(f'{height[i]} {height[j]}')
        cur = (j - i) * min(height[i], height[j])
        if maxArea < cur:
          maxArea = cur

      print('----')

    return maxArea

sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7])) 