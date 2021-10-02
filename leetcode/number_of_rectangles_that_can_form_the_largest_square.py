from typing import List

class Solution:
  def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
    maxL = 0
    count = 0
    for rec in rectangles:
      curMin = min(rec[0], rec[1])
      if curMin > maxL: 
        maxL = curMin
        count = 1
      elif curMin == maxL:
        count += 1
    # print(f'{count}')
    return count
sol = Solution()
assert sol.countGoodRectangles([[5,8],[3,9],[5,12],[16,5]]) == 3
assert sol.countGoodRectangles([[2,3],[3,7],[4,3],[3,7]]) == 3
assert sol.countGoodRectangles([[2,3],[3,1],[4,3],[3,7]]) == 2
assert sol.countGoodRectangles([[2,3],[3,1],[4,3],[3,7],[5,8]]) == 1
assert sol.countGoodRectangles([[2,3]]) == 2
