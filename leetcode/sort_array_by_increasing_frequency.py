from typing import List

class Solution:
  def frequencySort(self, nums: List[int]) -> List[int]:
    freq = {}
    for num in nums:
      if not num in freq:
        freq[num] = 0
      freq[num] += 1
    buckets = [[] for i in range(len(nums) + 1)]
    for key, val in freq.items():
      buckets[val].append(key)
    res = []
    for index, bucket in enumerate(buckets):
      if bucket:
        sortedBucket = sorted(bucket, key= lambda x: -x)
        # print(f'sortedBucket {sortedBucket}')
        for j in sortedBucket:
          for k in range(index):
            res.append(j)
    # print(f'{res}')
    return res
        
        
sol = Solution()
assert sol.frequencySort([1,1,2,2,2,3]) == [3,1,1,2,2,2]
assert sol.frequencySort([2,3,1,3,2]) == [1,3,3,2,2]
assert sol.frequencySort([-1,1,-6,4,5,-6,1,4,1]) == [5,-1,4,4,-6,-6,1,1,1]
assert sol.frequencySort([-1]) == [-1]
assert sol.frequencySort([1]) == [1]
