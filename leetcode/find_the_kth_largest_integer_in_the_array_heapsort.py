from typing import List
from heapq import heappush, heappop

class Solution:
  def kthLargestNumber(self, nums: List[str], k: int) -> str:
    minHeap = []
    for x in nums:
      heappush(minHeap, int(x))
      if len(minHeap) > k:
        heappop(minHeap)
    return str(heappop(minHeap))

sol = Solution()
assert sol.kthLargestNumber(["1","2","2"], 2) == "2"
assert sol.kthLargestNumber(["1","2","2"], 3) == "1"
assert sol.kthLargestNumber(["1","2","2"], 1) == "2"
assert sol.kthLargestNumber(["3","6","7","10"], 4) == "3"
assert sol.kthLargestNumber(["2","21","12","1"], 3) == "2"
assert sol.kthLargestNumber(["0", "0"], 2) == "0"
assert sol.kthLargestNumber(["0"], 1) == "0"
