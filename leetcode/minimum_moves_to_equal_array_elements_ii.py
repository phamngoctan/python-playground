from typing import List

class Solution:
  def minMoves2(self, nums: List[int]) -> int:
    newNums = sorted(nums)
    mid = newNums[len(newNums) // 2]
    res = 0
    for num in newNums:
      res += abs(mid - num)
    # print(f'{res}')
    return res
sol = Solution()
assert sol.minMoves2([1,2,3]) == 2
assert sol.minMoves2([1,10,2,9]) == 16
assert sol.minMoves2([-1,2,9]) == 10
assert sol.minMoves2([1,-2,10]) == 12
assert sol.minMoves2([-1,-2,-10]) == 9
