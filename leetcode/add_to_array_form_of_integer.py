from typing import List

class Solution:
  def addToArrayForm(self, num: List[int], k: int) -> List[int]:
    kStr = str(k)[::-1]
    res = [0 for i in range(max(len(num), len(kStr)) + 1)]
    num = num[::-1]
    position = len(res) - 1
    for i in range(len(res)):
      iAtNum = num[i] if i < len(num) else 0
      iAtK = kStr[i] if i < len(kStr) else 0
      res[position] += int(iAtNum) + int(iAtK)
      res[position - 1] += res[position] // 10
      res[position] = res[position] % 10
      position -= 1
    if res[0]:
      return res
    return res[1:]
    
sol = Solution()
assert sol.addToArrayForm(num = [1,2,0,0], k = 34) == [1,2,3,4]
assert sol.addToArrayForm(num = [2,7,4], k = 181) == [4,5,5]
assert sol.addToArrayForm(num = [2,1,5], k = 806) == [1,0,2,1]
assert sol.addToArrayForm(num = [9,9,9,9,9,9,9,9,9,9], k = 1) == [1,0,0,0,0,0,0,0,0,0,0]
