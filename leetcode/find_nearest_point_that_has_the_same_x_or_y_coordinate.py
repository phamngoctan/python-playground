from typing import List

class Solution:
  def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
    MAX_VALUE = 10**5
    curMin = MAX_VALUE
    ans = -1
    for i, point in enumerate(points):
      curX, curY = point
      if curX == x or curY == y:
        distance = abs(curX - x) + abs(curY - y)
        if distance < curMin:
          curMin = distance
          ans = i
    # print(f'{ans}')
    return ans
sol = Solution()
assert sol.nearestValidPoint(x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]) == 2
assert sol.nearestValidPoint(x = 3, y = 4, points = [[3,4]]) == 0
assert sol.nearestValidPoint(x = 3, y = 4, points = [[2,3]]) == -1
