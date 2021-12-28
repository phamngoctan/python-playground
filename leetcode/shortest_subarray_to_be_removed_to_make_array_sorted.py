from typing import List

class Solution:
  def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
    '''
    So many edge cases, but the main idea is straightforward
    '''
    n = len(arr)
    left = 0
    while left < n - 1  and arr[left] <= arr[left + 1]:
      left += 1
    
    # without this, the below code will resulted as -1
    if left == n - 1: return 0
    
    right = n - 1
    while right > left and arr[right] >= arr[right - 1]:
      right -= 1
    
    i, j = 0, right
    ans = min(n - left - 1, right)
    while i <= left and j <= n - 1: # should check until it reaches the left or the very right (=n - 1)
      if arr[j] >= arr[i]:
        ans = min(j - i - 1, ans) # only consider the ans when arr[j] >= arr[i]
        i += 1
      else:
        j += 1
    
    # print(f'{ans}')
    return ans
sol = Solution()
assert sol.findLengthOfShortestSubarray([1,2,3,10,4,2,3,5]) == 3
assert sol.findLengthOfShortestSubarray([5,4,3,2,1]) == 4
assert sol.findLengthOfShortestSubarray([1,2,3]) == 0
assert sol.findLengthOfShortestSubarray([1,2,3,10,1,2,3,4,5,6,7,8,9,10,4,2,3,5]) == 13
assert sol.findLengthOfShortestSubarray([10,1,2,3,4,2]) == 5
