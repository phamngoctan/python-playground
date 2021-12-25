from typing import List

class Solution:
  def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    (x1, y1), (x2, y2) = coordinates[: 2] # unpack in one line
    for x3, y3 in coordinates:
      if (x2 - x1) * (y3 - y2) != (x3 - x2) * (y2 - y1):
        return False
    return True
  
  def checkStraightLine_longCode(self, coordinates: List[List[int]]) -> bool:
    if len(coordinates) > 2:
      dx = coordinates[0][0] - coordinates[1][0]
      dy = coordinates[0][1] - coordinates[1][1]
      for i in range(2, len(coordinates)):
        newX, newY = coordinates[i]
        newDx = coordinates[0][0] - newX
        newDy = coordinates[0][1] - newY
        if dx * newDy != dy * newDx:
          return False
    return True
sol = Solution()
assert sol.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]) == True
assert sol.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]) == False
assert sol.checkStraightLine([[1,1],[2,2]]) == True
