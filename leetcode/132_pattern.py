from typing import List

class Solution:
  def find132pattern(self, nums: List[int]) -> bool:
    stack, s3 = [], -float("inf")
    for n in nums[::-1]:
      if n < s3: 
        return True
      while stack and stack[-1] < n: 
        s3 = stack.pop()
      stack.append(n)
    return False
  
  def find132pattern_notFullyWork(self, nums: List[int]) -> bool:
    '''
    Not work because we clean up the whole stack 
    while we still need to save the previous stac    k
    '''
    # if len(nums) < 3:
    #   return False
    monotonicStack = []
    for num in nums:
      while len(monotonicStack) > 0 and num < monotonicStack[-1]:
        monotonicStack.pop()
        if monotonicStack and num > monotonicStack[-1]:
          return True
      monotonicStack.append(num)
    return False
sol = Solution()
assert sol.find132pattern([7,9,10,3,18,16,8]) == True
# assert sol.find132pattern([1]) == False
# assert sol.find132pattern([1,2]) == False
# assert sol.find132pattern([5,6,4]) == False
# assert sol.find132pattern([3,6,4]) == True
# assert sol.find132pattern([1,2,3,4]) == False
# assert sol.find132pattern([3,1,4,2]) == True
# assert sol.find132pattern([-1,3,2,0]) == True
# assert sol.find132pattern([3,1,4,2,3]) == True
# assert sol.find132pattern([3,1,4,5,3]) == True
# assert sol.find132pattern([3,4,5,1]) == False
# assert sol.find132pattern([3,4,5,1,5]) == False
# assert sol.find132pattern([3,4,5,1,5,6,4]) == True
# assert sol.find132pattern([3,4,5,1,4]) == True
# assert sol.find132pattern([3,5,0,3,4]) == True
