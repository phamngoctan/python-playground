from typing import List

class Solution:
  def maxChunksToSorted(self, arr: List[int]) -> int:
    '''Greedy solution - prove by contradiction'''
    ans = 0
    maxSoFar = -1
    for i, num in enumerate(arr):
      maxSoFar = max(maxSoFar, num)
      if i == maxSoFar:
        ans += 1
    return ans
  
  def maxChunksToSorted_better(self, arr: List[int]) -> int:
    '''Greedy solution - prove by contradiction'''
    maxArr = []
    maxSoFar = -1
    for num in arr:
      maxSoFar = max(maxSoFar, num)
      maxArr.append(maxSoFar)
    ans = 0
    for i, num in enumerate(arr):
      if i == maxArr[i]:
        ans += 1
    return ans

  def maxChunksToSorted_goodIdeaFromLC(self, arr: List[int]) -> int:
    '''
    Borrow solution from LC. Same same idea as QuickSort
    '''
    # # base case | don't need it
    # the input arr should always have at least one item
    # if not arr:
    #   return 0
    
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
    return max(result) if result else 1
  
sol = Solution()
assert sol.maxChunksToSorted([4,3,2,1,0]) == 1
# for example [2,0,1,3,4]
# wrong approach, -> [2,0] [1,3,4]
# [0,2] [1,3,4] -> [0] [1,2] [3,4] =)) totally misunderstanding the problem

# we need to sort [2,0,1] [3,4]
# for [2,0,1] -> cannot divide to smaller chunks -> 1 big chunk of three items
# for [3,4] -> we don't want to keep it in one chunk, it will be reversed to [4,3]
# -> split to 2 chunks [3] and [4] -> base case is arr with length 1 -> return 1
assert sol.maxChunksToSorted([2,0,1,3,4]) == 3
