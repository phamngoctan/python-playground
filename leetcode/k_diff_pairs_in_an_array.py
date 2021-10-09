from typing import List

class Solution:
  def findPairs(self, nums: List[int], k: int) -> int:
    freq = {}
    for num in nums:
      if not num in freq:
        freq[num] = 0
      freq[num] += 1
    res = 0
    for key, val in freq.items():
      if (key - k) in freq:
        if (k == 0 and freq[key - k] > 1) or k > 0:
          res += 1
      if (key + k) in freq:
        if (k == 0 and freq[key + k] > 1) or k > 0:
          res += 1
    # print(f'{res//2}')
    return res // 2
sol = Solution()
assert sol.findPairs([3,1,4,1,5], k = 2) == 2
assert sol.findPairs([1,2,3,4,5], k = 1) == 4
assert sol.findPairs([1,3,1,5,4], k = 0) == 1
assert sol.findPairs([1,2,4,4,3,3,0,9,2,3], k = 3) == 2
assert sol.findPairs([-1,-2,-3], k = 1) == 2
assert sol.findPairs([-1,-2,-3], k = 1) == 2