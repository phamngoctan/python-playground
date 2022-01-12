from typing import List

class Solution:
  def finalPrices(self, prices: List[int]) -> List[int]:
    stack = []
    for i, val in enumerate(prices):
      while stack and prices[stack[-1]] >= val:
        poppedIndex = stack.pop()
        prices[poppedIndex] -= val
      stack.append(i)
    return prices
  
  def finalPrices_1(self, prices: List[int]) -> List[int]:
    monotonicStack = []
    ans = [0 for _ in range(len(prices))]
    for i, val in enumerate(prices): # round 1
      while monotonicStack and prices[monotonicStack[-1]] >= val:
        poppedIndex = monotonicStack.pop()
        ans[poppedIndex] = prices[poppedIndex] - val
      monotonicStack.append(i)
      
    while monotonicStack: # round 2
      poppedIndex = monotonicStack.pop()
      ans[poppedIndex] = prices[poppedIndex]
    # print(f'{ans}')
    return ans

sol = Solution()
assert sol.finalPrices([8,4,6,2,3]) == [4,2,4,2,3]
assert sol.finalPrices([1,2,3,4,5]) == [1,2,3,4,5]
assert sol.finalPrices([10,1,1,6]) == [9,0,1,6]
