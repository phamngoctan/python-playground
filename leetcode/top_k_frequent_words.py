from typing import List
from heapq import heappush, heappushpop, heappop

class Solution:
  def topKFrequent(self, words: List[str], k: int) -> List[str]:
    freq = {}
    for word in words:
      if word not in freq:
        freq[word] = 0
      freq[word] += 1
    # print(f'{freq}')
    pq = []
    for key, val in freq.items():
      if len(pq) == k:
        heappushpop(pq, Item(val, key))
      else:
        heappush(pq, Item(val, key))
    tmp = []
    while len(pq) > 0:
      item = heappop(pq)
      tmp.append(item.key)
    res = tmp[::-1]
    # print(f'{res}')
    return res

class Item:
  def __init__(self, count, key):
    self.frequency = count
    self.key = key
  def __lt__(self, other):
    if self.frequency != other.frequency:
      return self.frequency < other.frequency
    else:
      return self.key > other.key

sol = Solution()
assert sol.topKFrequent(["i","love","leetcode","i","love","coding"], k = 2) == ['i', 'love']
assert sol.topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4) == ["the","is","sunny","day"]
assert sol.topKFrequent(["is","is"], k = 1) == ["is"]
assert sol.topKFrequent(["is"], k = 1) == ["is"]
