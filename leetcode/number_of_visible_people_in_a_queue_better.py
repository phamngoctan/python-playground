from typing import List

class Solution:
  def canSeePersonsCount(self, heights: List[int]) -> List[int]:
    stack = []
    res = [0 for _ in range(len(heights))]
    for i in range(len(heights) - 1, -1, -1):
      while len(stack) > 0 and stack[-1] < heights[i]:
        stack.pop()
        res[i] += 1 # each popped out element is the one has been seen by current position
      if stack: # in case the current value is not the highest value (it will see the next greater value)
        res[i] += 1
      stack.append(heights[i])
    return res
sol = Solution()
assert sol.canSeePersonsCount([10,6,8,5,11,9]) == [3,1,2,1,1,0]
assert sol.canSeePersonsCount([5,1,2,3,10]) == [4,1,1,1,0]
