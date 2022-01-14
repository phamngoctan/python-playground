from typing import List

class Solution:
  def sumSubarrayMins(self, A: List[int]) -> int:
    # input is [3,1,2,4]
    n = len(A)
    mod = 10**9 + 7
    previousLess = [i + 1 for i in range(n)] # [1,2,3,4]
    nextLess = [n - i for i in range(n)] # [4,3,2,1]
    mStack1, mStack2 = [], []
    for i in range(n):
      # fopr previous less
      while mStack1 and mStack1[-1][0] > A[i]:
        mStack1.pop()
      if mStack1: # if there is no previous less then, keep the position value of each item
        previousLess[i] = i - mStack1[-1][1]
      mStack1.append([A[i], i])
      
      # for next less than 
      # has same idea as easy problem Final Prices With a Special Discount in a Shop
      # put current item to stack and if the new item less than value, pop it out
      while mStack2 and mStack2[-1][0] > A[i]:
        _, prevItemIndex = mStack2.pop()
        nextLess[prevItemIndex] = i - prevItemIndex
      mStack2.append([A[i], i])
    
    print(f'{previousLess}') 
    # in stack1 we have [[1, 1], [2, 2], [4, 3]]
    # [1,2,1,1] the first index, we pop it out 
    # but no item left in stack (no lesser value of previous item) -> keep the original value in ans
    print(f'{nextLess}')
    # in stack2 we have [[1, 1], [2, 2], [4, 3]] - the ones we are not touch
    # [1,3,2,1] not touch the 3 last position (keep the original value)
    ans = 0
    for i in range(n):
      ans = (ans + A[i]*previousLess[i]*nextLess[i]) % mod
    print(f'{ans}')
    return ans
  
  """
  Must be re-implementation -> Done the re-implementation -> Cheer
  """
  def sumSubarrayMins_cleanButHardToUnderstand(self, A: List[int]) -> int:
    A = [0]+A
    result = [0]*len(A)
    stack = [0]
    for i in range(len(A)):
      while A[stack[-1]] > A[i]:
        stack.pop() 
      j = stack[-1]
      result[i] = result[j] + (i-j)*A[i]
      stack.append(i)
    return sum(result) % (10**9+7)
  
sol = Solution()
assert sol.sumSubarrayMins([3,1,2,4]) == 17
