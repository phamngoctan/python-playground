from typing import List

class Solution:
  '''
  Very good idea to use the i - 1 - monotonicStack[-1] =))
  I haven't realised that until debugging
  '''
  def largestRectangleArea(self, heights: List[int]) -> int:
    monotonicStack = [-1] # the reference for the very first position, before 0 is -1
    heights.append(0) # make sure the last item in the list is considered to be popped out
    ans = 0
    for i in range(len(heights)):
      while heights[i] < heights[monotonicStack[-1]]:
        height = heights[monotonicStack.pop()]
        width = i - 1 - monotonicStack[-1] # go to the very very previous position, not the right one before
        ans = max(ans, height * width)
      monotonicStack.append(i)
    # print(f'{ans}')
    return ans

sol = Solution()
assert sol.largestRectangleArea([0]) == 0
assert sol.largestRectangleArea([2]) == 2
assert sol.largestRectangleArea([2,1,5,6,2,3]) == 10
assert sol.largestRectangleArea([2,1,5,0,2,3]) == 5
assert sol.largestRectangleArea([2,1,5,6,2,3,0,1,1]) == 10
assert sol.largestRectangleArea([2,1,5,6,2,3,2,3]) == 12
assert sol.largestRectangleArea([2,1,5,6,3,3,3,3,3,4,2,2,2,2,2,2,2,2]) == 32
