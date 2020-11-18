class Solution:
    def subtractProductAndSum(self, n: int) -> int:
      asterisk = 1
      sum = 0
      arr = list(str(n))
      for i in arr:
        sum += int(i)
        asterisk *= int(i)
      return asterisk - sum
s = Solution()
print(s.subtractProductAndSum(234))
print(s.subtractProductAndSum(4421))