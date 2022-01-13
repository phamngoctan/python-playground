from typing import List

class Solution:
  def trap_twoPointers(self, height: List[int]) -> int:
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
  
  def trap(self, height: List[int]) -> int:
    """
    Different view of the trapped water, instead of viewing vertically,
    we view the problem in horizontally
    """
    ans, mStack = 0, []
    for i in range(len(height)):
      while mStack and height[i] > height[mStack[-1]]:
        h = height[mStack.pop()]
        if mStack:
          minH = min(height[mStack[-1]], height[i])
          ans += (minH - h)*(i - mStack[-1] - 1)
      mStack.append(i)
    return ans

sol = Solution()
assert sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
sol.trap([4,2,0,3,5]) == 7
sol.trap([4,2,0,3,2,5]) == 9
sol.trap([9,8,7,6,5,4,3,2,1]) == 0
sol.trap([4,2,3]) == 1
sol.trap([4,2]) == 0


