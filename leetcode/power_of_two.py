class Solution:
  def isPowerOfTwo(self, n: int) -> bool:
    if n <= 0: return False
    return (n & n - 1) == 0
    
  def isPowerOfTwo_withLoop(self, n: int) -> bool:
    if n == 0: return False
    while n % 2 == 0:
        n = n // 2
    return n == 0 or n == 1

sol = Solution()
assert sol.isPowerOfTwo(0) == False
assert sol.isPowerOfTwo(1) == True
assert sol.isPowerOfTwo(2) == True
assert sol.isPowerOfTwo(3) == False
assert sol.isPowerOfTwo(7) == False
assert sol.isPowerOfTwo(8) == True
assert sol.isPowerOfTwo(10) == False
assert sol.isPowerOfTwo(16) == True
