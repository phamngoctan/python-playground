from typing import List
from heapq import heappush, heappop

class Solution:
  def maxEvents(self, events: List[List[int]]) -> int:
    ans = 0
    minHeap = [] # min heap of events end time
    events = sorted(events, key= lambda x: x[0]) # sort events by start time
    i = 0 # counter in events arr
    curDay = 0
    while i < len(events) or minHeap:
      if not minHeap:
        curDay = events[i][0] # jump the curDay
      
      while i < len(events) and events[i][0] <= curDay:
        # add open events for curDay
        heappush(minHeap, events[i][1])
        i += 1
      
      heappop(minHeap) # attend the event ends earliest
      ans += 1
      
      curDay += 1
      # remove close events for cur_day
      # this can remove the un-attendable events
      # i.e: [1,1],[1,2],[2,2]
      # at day 2, we can only attend event [1,2]
      # the last one will be removed (curDay now is 3)
      while minHeap and minHeap[0] < curDay:
        heappop(minHeap)
    return ans
  
sol = Solution()
assert sol.maxEvents([[1,2],[1,1],[2,2]]) == 2
assert sol.maxEvents([[1,2],[2,3],[3,4]]) == 3
assert sol.maxEvents([[1,2],[2,3],[3,4],[1,2]]) == 4
