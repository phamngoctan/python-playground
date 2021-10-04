from typing import List

class Solution:
  def largestSumAfterKNegations(self, A, K):
    A.sort()
    i = 0
    while i < len(A) and i < K and A[i] < 0:
        A[i] = -A[i]
        i += 1
    return sum(A) - (K - i) % 2 * min(A) * 2

sol = Solution()
assert sol.largestSumAfterKNegations([4,2,3], 1) == 5
assert sol.largestSumAfterKNegations([3,-1,0,2], 3) == 6
assert sol.largestSumAfterKNegations([2,-3,-1,5,-4], 4) == 13
assert sol.largestSumAfterKNegations([2,-3,-1,5,-4], 2) == 13
assert sol.largestSumAfterKNegations([2,-3,-1,5,-4], 3) == 15
