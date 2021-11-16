from typing import List
class Solution:
  def findMinArrowShots(self, points: List[List[int]]) -> int:
    points.sort(key = lambda x: (x[0], -x[1]))
    count = 1
    lastEnd = points[0]
    # print(f'{points}')
    for s, e in points[1:]:
      if lastEnd[1] > e:
        lastEnd = [min(lastEnd[1], s),min(lastEnd[1], e)]
        continue
      if lastEnd[1] >= s:
        lastEnd = [s,lastEnd[1]]
      else:
        count += 1
        lastEnd = [s, e]
    # print(f'{count}')
    return count
sol = Solution()
assert sol.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]) == 2
assert sol.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]) == 4
assert sol.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]) == 2
assert sol.findMinArrowShots([[1,2],[2,3],[3,4],[4,5],[1,6]]) == 2
assert sol.findMinArrowShots([[-1000,100],[-100,99],[-80,102],[0,10],[98,1000]]) == 2
assert sol.findMinArrowShots([[-2147483646,-2147483645],[2147483646,2147483647]]) == 2
