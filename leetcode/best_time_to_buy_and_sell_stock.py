from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    curMin = 10**5 + 1
    res = 0
    for price in prices:
      curMin = min(curMin, price)
      if price > curMin:
        res = max(res, price - curMin)
    # print(f'{res}')
    return res
sol = Solution()
assert sol.maxProfit([7,1,5,3,6,4]) == 5
assert sol.maxProfit([1,5,3,6,4,8,6,1,10]) == 9
assert sol.maxProfit([0, 6, -3, 7]) == 10
