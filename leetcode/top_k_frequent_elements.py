from typing import List
from heapq import heappush, heappushpop, heappop

class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    freq = {}
    for num in nums:
      if not num in freq:
        freq[num] = 0
      freq[num] += 1
    buckets = [[] for _ in range(len(nums) + 1)]
    for key, val in freq.items():
      buckets[val].append(key)
    res = []
    for i in range(len(nums), 0, -1):
      if len(buckets[i]) > 0:
        res.extend(buckets[i])
      if len(res) >= k:
        break
    return res

    
  def topKFrequentUsingPriorityQueue(self, nums: List[int], k: int) -> List[int]:
    freq = {}
    for num in nums:
      if not num in freq:
        freq[num] = 0
      freq[num] += 1
    pq = []
    for key, val in freq.items():
      if len(pq) == k:
        heappushpop(pq, (val, key))
      else:
        heappush(pq, (val, key))
    # print(pq)
    mostFreq = []
    while len(pq) > 0:
      mostFreq.append(heappop(pq)[1])
    res = mostFreq[::-1]
    # print(f'{res}')
    return res
    
sol = Solution()
assert sol.topKFrequent([1,1,1,2,2,3,4,5,6,7,8], k = 2) == [1,2]
assert sol.topKFrequent([1,1,1,2,1,3,3], k = 2) == [1,3]
assert sol.topKFrequent([1], k = 1) == [1]
assert sorted(sol.topKFrequent([1,1,2,2,3,10**5], k = 2)) == [1,2]
assert sorted(sol.topKFrequent([-1,-1,2,2,3,10**5], k = 2)) == [-1,2]
assert sorted(sol.topKFrequent([-1,-1,2,5,3,3], k = 2)) == [-1,3]
