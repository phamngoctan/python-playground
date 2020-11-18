class Solution:
    def subtractProductAndSum(self, n: int) -> int:
      asterisk = 1
      sum = 0
      while n:
        cur = n % 10
        asterisk *= cur
        sum += cur
        n = n // 10
      return asterisk - sum
s = Solution()
print(s.subtractProductAndSum(234))
print(s.subtractProductAndSum(4421))