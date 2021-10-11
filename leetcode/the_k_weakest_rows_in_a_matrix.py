from typing import List
from heapq import heappushpop, heappush, heappop

class Solution:
  def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    heap = [] # Size: O(k)
    # Iterate over the rows in O(m).
    for index, row in enumerate(mat):
      soldier_count = self.soldier_count(row)
      # Push values to the heap in O(log k)
      if len(heap) == k:
        heappushpop(heap, (-soldier_count, -index))
      else:
        heappush(heap, (-soldier_count, -index))
    
    weakest_rows = [] # Size: O(k)
    # Push the heap values into our result list in O(k log k).
    while heap:
      weakest_rows.append(-heappop(heap)[1])
    # Return the result in reversed order.
    return weakest_rows[::-1]
    
  # Find the number of soldiers in a row using Binary Search in O(log n).
  def soldier_count(self, row: List[int]) -> int:
    low, high = 0, len(row) - 1

    while low < high:
      mid = (low + high + 1) // 2
      if not row[mid]:
        high = mid - 1
      else:
        low = mid
    # We need to return a count and not an index.
    # Therefore we need to increase the result by one if soldiers have been found.
    if row[0]:
      low += 1
    return low
      
sol = Solution()
assert sol.kWeakestRows(
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3) == [2,0,3]

assert sol.kWeakestRows(
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2) == [0,2]