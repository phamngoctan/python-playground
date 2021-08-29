from typing import List

class Solution:
  def trap(self, height: List[int]) -> int:
    maxWater = 0
    for i in range(0, len(height)):
      p1 = i - 1
      p2 = i + 1
      maxP1 = height[p1] if i - 1 >= 0 else 0
      maxP2 = height[p2] if i + 1 < len(height) else 0
      
      while p1 >= 0:
        maxP1 = max(height[p1], maxP1)
        # print(f'p1 is {p1}')
        p1 -= 1
      
      while p2 < len(height):
        maxP2 = max(height[p2], maxP2)
        # print(f'p2 is {p2}')
        p2 += 1

      # print('---------------')
      # print(f'{min(maxP1, maxP2) - height[i]} {maxP1} {maxP2}')
      if min(maxP1, maxP2) - height[i] > 0:
        maxWater += min(maxP1, maxP2) - height[i]

    return maxWater

sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(sol.trap([4,2,0,3,2,5])) # 9
print(sol.trap([9,8,7,6,5,4,3,2,1])) # 0
print(sol.trap([4,2,3])) # 1
