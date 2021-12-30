from typing import List

class Solution:
  def maxChunksToSorted(self, arr: List[int]) -> int:
    '''
    clearest
    '''
    stack = [] # range of item
    for i in range(len(arr)):
      cur = [arr[i], arr[i]]
      while stack and stack[-1][0] > cur[1]:
        pre = stack.pop()
        cur[0] = max(cur[0], pre[0])
        cur[1] = min(cur[1], pre[1])
      stack.append(cur)
    # print(f'{len(stack)}')
    return len(stack)
  
  def maxChunksToSorted_maxPreviousStack(self, arr: List[int]) -> int:
    '''
    Without using the previous min
    '''
    stack = [] # range of item
    for i in range(len(arr)):
      cur = arr[i]
      while stack and stack[-1] > arr[i]:
        pre = stack.pop()
        cur = max(arr[i], pre)
      stack.append(cur)
    return len(stack)
  
  def maxChunksToSorted_bestPerformance(self, arr: List[int]) -> int:
    '''
    Keep the maxOfLeft and minOfRight, at any i, if maxOfLeft <= minOfRight[i+1]
    => it a new chunk -> ans += 1
    return ans + 1
    '''
    maxOfLeft = [0 for _ in range(len(arr))]
    maxSoFar = -1
    for i, num in enumerate(arr):
      maxSoFar = max(maxSoFar, num)
      maxOfLeft[i] = maxSoFar
    
    minOfRight = [0 for _ in range(len(arr))]
    minSoFar = float('inf')
    for i in range(len(arr) - 1, -1, -1):
      minSoFar = min(minSoFar, arr[i])
      minOfRight[i] = minSoFar
    ans = 0
    # print(f'{maxOfLeft}')
    # print(f'{minOfRight}')
    for i in range(len(arr) - 1):
      if maxOfLeft[i] <= minOfRight[i + 1]:
        ans += 1
    # print(f'{ans}')
    return ans + 1
  
  def maxChunksToSorted_bruceForce(self, arr: List[int]) -> int:
    '''
    Borrow solution from LC. Same same idea as QuickSort
    '''
    if len(arr) == 1: # base case
      return 1
    result = []
    for pivot in range(1, len(arr)):
      left = arr[:pivot]
      right = arr[pivot:]
      if sorted(left) + sorted(right) == sorted(arr):
        result.append(self.maxChunksToSorted(left) + self.maxChunksToSorted(right))
    # in case [1,2,0], it is all mess
    # no pivot can form the sorted arr
    # so 1 big chunk can be formed and sorted once
    # => return 1
    # print(f'{max(result) if result else 1}')
    return max(result) if result else 1

sol = Solution()
assert sol.maxChunksToSorted([5,1,1,8,4]) == 1
assert sol.maxChunksToSorted([5,1,1,8,6]) == 2
assert sol.maxChunksToSorted([5,1,1,8,1,6,5,9,7,8]) == 1
assert sol.maxChunksToSorted([1]) == 1
assert sol.maxChunksToSorted([1,3,5]) == 3
assert sol.maxChunksToSorted([5,4,3,2,1]) == 1
assert sol.maxChunksToSorted([2,1,3,4,4]) == 4
assert sol.maxChunksToSorted([1,1,0,0,1]) == 2
assert sol.maxChunksToSorted([68,46,20,65,19,97,74,76,14,26,162,176,130,197,192,113,177,110,103,181,288,295,296,276,231,210,209,206,250,283,376,298,300,357,310,377,349,394,341,303,399,419,447,429,418,446,408,401,432,488,496,538,559,559,521,499,564,496,544,524,598,626,676,677,613,659,676,682,663,669,704,764,791,765,791,780,723,716,761,738,877,888,838,870,865,808,884,862,878,888,893,916,970,903,967,952,974,936,958,928]) == 17
