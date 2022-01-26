from typing import List

class Solution:
  def validMountainArray_myIdea(self, arr: List[int]) -> bool:
    """ Check the next 
    """
    n = len(arr)
    if n < 3: return False
    i = 0
    while i < n - 1 and arr[i] < arr[i + 1]:
      i += 1
    if i == n - 1 or i == 0:
      return False

    while i < n - 1 and arr[i] > arr[i + 1]:
      i += 1
    if i == n - 1:
      return True
    return False

sol = Solution()
assert sol.validMountainArray([2,1]) == False
assert sol.validMountainArray([3,5,5]) == False
assert sol.validMountainArray([3,5,4]) == True
assert sol.validMountainArray([0,3,2,1]) == True
assert sol.validMountainArray([0,2,3,4,5,2,1,0]) == True
assert sol.validMountainArray([0,1,2,3,4,5,6,7,8,9]) == False
assert sol.validMountainArray([9,8,7,6,5,4,3,2,1,0]) == False
