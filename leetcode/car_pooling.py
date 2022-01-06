from typing import List
from heapq import heappush, heappop

class Solution:
  def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
    stops = [0 for _ in range(1001)]
    for noPassengers, startTime, endTime in trips:
      stops[startTime] += noPassengers
      stops[endTime] -= noPassengers
    for stop in stops:
      capacity -= stop
      if capacity < 0:
        return False
    return True
  
  def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
    trips.sort(key= lambda x: x[1]) # sort by start time
    totalPassengers = 0
    minHeap = [] # heap by endTime and number of passengers
    for trip in trips:
      numPassengers, start, end = trip
      while minHeap and minHeap[0][0] <= start:
        totalPassengers -= minHeap[0][1]
        heappop(minHeap)
      heappush(minHeap, [end, numPassengers])
      totalPassengers += numPassengers
      if totalPassengers > capacity:
        return False
    return True

sol = Solution()
assert sol.carPooling([[2,1,2],[3,3,7]], 4) == True
assert sol.carPooling([[2,1,3],[3,3,7]], 4) == True
assert sol.carPooling([[2,1,5],[3,3,7]], 4) == False
assert sol.carPooling([[2,1,5],[3,3,7]], 5) == True
assert sol.carPooling([[2,1,5],[3,5,7]], 3) == True
assert sol.carPooling([[3,2,7],[3,7,9],[8,3,9]], 11) == True
