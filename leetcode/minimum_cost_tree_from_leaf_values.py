from typing import List

class Solution:
  def mctFromLeafValues(self, nums):
    res = 0
    MAX_VALUE = 16
    monotonicStack = [MAX_VALUE] # trick to handle the first element
    for num in nums:
      while len(monotonicStack) > 0 and num > monotonicStack[-1]:
        midValueNum = monotonicStack.pop()
        res += midValueNum * min(monotonicStack[-1], num)
      monotonicStack.append(num)
    while len(monotonicStack) > 2:
      res += monotonicStack.pop() * monotonicStack[-1]
    # print(f'{res}')
    return res
  
  def mctFromLeafValues_bruceforce(self, A):
    res = 0
    while len(A) > 1: # number of non-leaf node = total leave nodes - 1
      i = A.index(min(A))
      res += min(A[i - 1:i] + A[i + 1:i + 2]) * A.pop(i)
    # print(f'{res}')
    return res
  
sol = Solution()
assert sol.mctFromLeafValues([6,4,4,2,5]) == 74
assert sol.mctFromLeafValues([6,5,5,2,5]) == 90
assert sol.mctFromLeafValues([1,2,4]) == 10
assert sol.mctFromLeafValues([6,2,4]) == 32
assert sol.mctFromLeafValues([6,2,4,5]) == 58
assert sol.mctFromLeafValues([5,4,4,3,2,1]) == 56
