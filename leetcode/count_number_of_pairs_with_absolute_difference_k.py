from typing import List

class Solution:
  def countKDifference(self, nums: List[int], k: int) -> int:
    freq = {}
    for num in nums:
      if not num in freq:
        freq[num] = 0
      freq[num] += 1
    total = 0
    for key, val in freq.items():
      if key - k in freq:
        total += val * freq[key - k]
      if key + k in freq:
        total += val * freq[key + k]
    return total//2
sol = Solution()
assert sol.countKDifference([1,2,2,1], 1) == 4
assert sol.countKDifference([1,3], 3) == 0
assert sol.countKDifference([3,2,1,5,4], 2) == 3
assert sol.countKDifference([3,2,1,5,4,4,4], 2) == 5
