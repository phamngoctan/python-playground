from typing import List

class Solution:
  def trap(self, height: List[int]) -> int:
    maxWater = 0
    # for i in range(0, len(height)):
    i = 0
    # print(f'length: {len(height)}')
    while i < len(height):
      # p1 = i - 1
      # p2 = i + 1
      # maxP1 = height[p1] if i - 1 >= 0 else 0
      # maxP2 = height[p2] if i + 1 < len(height) else 0
      
      # while p2 < len(height):
      #   maxP2 = max(height[p2], maxP2)
      #   # print(f'p2 is {p2}')
      #   p2 += 1

      # # print('---------------')
      # while (p1 < p2):
      #   print(f'{min(maxP1, maxP2) - height[i]} {maxP1} {maxP2}')
      #   if min(maxP1, maxP2) - height[i] > 0:
      #     maxWater += min(maxP1, maxP2) - height[i]
      #   p1 += 1
      cur = height[i + 1]
      j = i + 1
      while j < len(height) and height[j] < height[i]:
        cur = max(height[j], cur)
        j += 1
      # print(f'height[i]: {height[i]} cur {cur}')
      # print(f'next max position: {j}')

      poolHeight = min(height[j] if j < len(height) else cur, height[i])
      while i < j:
        # print(f'{poolHeight} {j} {height[i]} water is {poolHeight - height[i]}')
        if poolHeight - height[i] > 0:
          maxWater += poolHeight - height[i]
        i += 1

      # print(f'current i is: {i}')
    return maxWater

sol = Solution()
# print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(sol.trap([4,2,0,3,2,5])) # 9
print(sol.trap([9,8,7,6,5,4,3,2,1])) # 0
print(sol.trap([4,2,3])) # 1


