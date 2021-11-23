class Solution:
  def isUgly(self, n:int):
    if n <= 0:
      return False
    for i in 2,3,5:
      while n % i == 0:
        n /= i
    return n == 1
  
  def isUgly_geekForGeek(self, n: int) -> bool:
    if n <= 0:
      return False
    num = self.maxDivide(n, 2)
    num = self.maxDivide(num, 3)
    num = self.maxDivide(num, 5)
    return True if num == 1 or num == -1  else False
  
  def maxDivide(self, a, b):
    while a % b == 0:
      a = a // b
    return a
sol = Solution()
assert sol.isUgly(-1) == False
assert sol.isUgly(0) == False
assert sol.isUgly(1) == True
assert sol.isUgly(-2) == False
assert sol.isUgly(2) == True
assert sol.isUgly(3) == True
assert sol.isUgly(4) == True
assert sol.isUgly(5) == True
assert sol.isUgly(6) == True
assert sol.isUgly(7) == False
assert sol.isUgly(8) == True
assert sol.isUgly(9) == True
assert sol.isUgly(10) == True
assert sol.isUgly(11) == False
assert sol.isUgly(12) == True
assert sol.isUgly(61440000) == True
assert sol.isUgly(79716150) == True
assert sol.isUgly(78643200) == True
assert sol.isUgly(78643201) == False
