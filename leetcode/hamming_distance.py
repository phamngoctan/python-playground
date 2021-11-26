class Solution:
  def hammingDistance(self, x: int, y: int) -> int:
    xor = x^y
    count = 0
    while xor > 0:
      count += 1 if xor % 2 == 1 else 0
      xor //= 2
    return count
  def hammingDistance_their(self, x: int, y: int) -> int:
    binaryStrOfXor = bin(x^y)
    count = 0
    for ch in binaryStrOfXor:
      count += 1 if ch == '1' else 0
    return count
  def hammingDistance_mine(self, x: int, y: int) -> int:
    count = 0
    while x > 0 and y > 0:
      if x % 2 != y % 2:
        count += 1
      x = x // 2
      y = y //2
    while x > 0:
      if x % 2 == 1:
        count += 1
      x = x // 2
    while y > 0:
      if y % 2 == 1:
        count += 1
      y = y // 2
    return count
sol = Solution()
assert sol.hammingDistance(x = 1, y = 4) == 2
assert sol.hammingDistance(x = 1, y = 3) == 1
