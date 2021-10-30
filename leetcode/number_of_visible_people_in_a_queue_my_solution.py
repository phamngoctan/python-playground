from typing import List

class Solution:
  def canSeePersonsCount(self, heights: List[int]) -> List[int]:
    # stack = [heights[len(heights) - 1]]
    stack = []
    res = [0 for _ in range(len(heights))]
    for i in range(len(heights) - 1, -1, -1):
      count = 0
      while len(stack) > 0 and stack[-1] < heights[i]:
        stack.pop()
        count += 1
      res[i] = count + (1 if len(stack) > 0 and stack[-1] > heights[i] else 0)
      stack.append(heights[i])
    # print(f'{res}')
    return res
sol = Solution()
assert sol.canSeePersonsCount([10,6,8,5,11,9]) == [3,1,2,1,1,0]
assert sol.canSeePersonsCount([5,1,2,3,10]) == [4,1,1,1,0]
