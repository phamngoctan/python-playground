class Solution:
  def rangeBitwiseAnd(self, left: int, right: int) -> int:
    i = 0
    while left != right:
      left >>= 1
      right >>= 1
      i += 1
    return left << i
sol = Solution()
assert sol.rangeBitwiseAnd(left = 5, right = 7) == 4
assert sol.rangeBitwiseAnd(left = 0, right = 0) == 0
assert sol.rangeBitwiseAnd(left = 1, right = 2147483647) == 0
