class Solution:
  def mySqrt(self, x: int) -> int:
    if x == 0:
      return 0
    left = 1
    right = x
    res = None
    while left <= right:
      mid = left + (right - left)//2
      if mid <= x/mid:
        left = mid + 1
        res = mid
      else:
        right = mid - 1
    return res
sol = Solution()
assert sol.mySqrt(4) == 2
assert sol.mySqrt(8) == 2
