from typing import List

class Solution:
  def trap(self, height: List[int]) -> int:
    maxWater = 0
    pl = 0
    pr = len(height) - 1
    maxL = height[pl]
    maxR = height[pr]
    while (pl < pr):
      # print(f'left pointer {pl}')
      # print(f'right pointer {pr}')
      maxL = max(maxL, height[pl])
      maxR = max(maxR, height[pr])
      # print(f'maxWater {maxWater}')
      addedWater = 0
      if maxL <= maxR:
        addedWater = maxL - height[pl]
        pl += 1
      else:
        addedWater = maxR - height[pr]
        pr -= 1

      maxWater += addedWater if addedWater > 0 else 0
      # print('--------')
    return maxWater

sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(sol.trap([4,2,0,3,2,5])) # 9
print(sol.trap([9,8,7,6,5,4,3,2,1])) # 0
print(sol.trap([4,2,3])) # 1
print(sol.trap([4,2])) # 0


