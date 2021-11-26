class Solution:
  def nthUglyNumber(self, n: int) -> int:
    ans = [0 for _ in range(n)]
    ans[0] = 1
    indexAtFactor2, indexAtFactor3, indexAtFactor5 = 0,0,0
    factor2, factor3, factor5 = 2, 3, 5
    for i in range(1, n):
      minOfFactor = min(min(factor2, factor3), factor5)
      ans[i] = minOfFactor
      if minOfFactor == factor2:
        indexAtFactor2 += 1
        factor2 = ans[indexAtFactor2] * 2
      if minOfFactor == factor3:
        indexAtFactor3 += 1
        factor3 = ans[indexAtFactor3] * 3
      if minOfFactor == factor5:
        indexAtFactor5 += 1
        factor5 = ans[indexAtFactor5] * 5
    # print(f'{ans}')
    return ans[n - 1]
  
  def nthUglyNumber_TLE_version(self, n: int) -> int:
    if n == 1:
      return 1
    count = 1
    i = 2
    while True:
      if self.isUgly(i):
        count += 1
      if count == n:
        return i
      i += 1
  
  def maxDivide(self, a, b):
    while a % b == 0:
      a = a//b
    return a

  def isUgly(self, num):
    num = self.maxDivide(num, 2)
    num = self.maxDivide(num, 3)
    num = self.maxDivide(num, 5)
    return True if num == 1 else False

sol = Solution()
assert sol.nthUglyNumber(10) == 12
assert sol.nthUglyNumber(1) == 1
assert sol.nthUglyNumber(11) == 15
assert sol.nthUglyNumber(1069) == 79716150
