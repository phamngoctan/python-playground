from typing import List
from heapq import heappush, heappop

class Solution:
  def maxTwoEvents(self, events: List[List[int]]) -> int:
    ans = 0
    most = 0
    minHeap = []
    for startTime, endTime, val in sorted(events):
      heappush(minHeap, [endTime, val])
      while minHeap and minHeap[0][0] < startTime:
        _, vv = heappop(minHeap)
        most = max(most, vv)
      ans = max(ans, most + val)
    return ans

  def maxTwoEvents_binarySearch(self, events: List[List[int]]) -> int:
    from bisect import bisect_left
    events = sorted(events, key= lambda x: x[1])
    # print(f'{events}')
    endTimes = []
    vals = [0 for _ in range(len(events))]
    vals[0] = events[0][2]
    for i in range(1, len(events)):
      vals[i] = max(vals[i - 1], events[i][2])
    # print(f'{vals}')
    ans = 0
    for st, et, val in events: 
      k = bisect_left(endTimes, st) - 1
      # with bisect_left
      # k will equals the endTime that matches with input startTime
      # or k is the very first bigger item (most left).
      # we minus 1 mean that it always delivers the previous event.
      # NOW, how do we get the max of all previous event???
      # we use the vals above (contains only maxSoFar)
      if k >= 0:
        val += vals[k]
      ans = max(ans, val)
      endTimes.append(et)
    # print(f'{ans}')
    return ans

sol = Solution()
assert sol.maxTwoEvents([[66,97,90],[98,98,68],[38,49,63],[91,100,42],[92,100,22],[1,77,50],[64,72,97]]) == 165
assert sol.maxTwoEvents([[1,2,5],[3,4,2],[2,7,3],[7,9,3]]) == 8
assert sol.maxTwoEvents([[1,3,2],[2,5,3],[5,6,2]]) == 4
assert sol.maxTwoEvents([[1,3,2],[4,5,2],[2,4,3]]) == 4
assert sol.maxTwoEvents([[1,3,2],[4,5,2],[1,5,5]]) == 5
assert sol.maxTwoEvents([[1,5,3],[1,5,1],[6,6,5]]) == 8
