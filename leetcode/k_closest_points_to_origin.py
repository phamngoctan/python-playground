from typing import List
from heapq import heappush, heappushpop
import math

class Solution:
  def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    minHeap = []
    for index, point in enumerate(points):
      x, y = point
      distance = math.sqrt(x * x + y * y)
      curPoint = [-distance, index, point]
      if len(minHeap) < k:
        heappush(minHeap, curPoint)
      else:
        heappushpop(minHeap, curPoint)
    ans = [x[2] for x in minHeap]
    # print(f'{ans}')
    return sorted(ans)
sol = Solution()
assert sol.kClosest([[1,3],[-2,2]], k = 1) == [[-2,2]]
assert sol.kClosest([[3,3],[5,-1],[-2,4]], k = 2) == [[-2, 4], [3, 3]]
assert sol.kClosest([[1,1],[2,2],[3,3],[-4,4]], k = 3) == [[1,1],[2,2],[3,3]]
