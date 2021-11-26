from typing import List

class Solution:
  def rotate(self, nums: List[int], k: int) -> None:
    def reverse(nums, start, end):
      while start < end:
        tmp = nums[start]
        nums[start] = nums[end]
        nums[end] = tmp
        start += 1
        end -= 1
    n = len(nums)
    k = k % n
    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)
    # print(f'{nums}')
  
  def rotate_borrowHalf_fromLeetcode(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    Time complexity: O(n)
    Space complexity: O(1)
    """
    n = len(nums)
    k = k % n
    i = 0
    start = 0
    curPosition = 0
    previousPosValue = nums[curPosition]
    while i < n:
      while True:
        newPosition = (curPosition + k) % n
        tmp = nums[newPosition]
        nums[newPosition] = previousPosValue
        previousPosValue = tmp
        curPosition = newPosition
        i += 1
        if curPosition == start:
          break
      start += 1
      curPosition = start % n
      previousPosValue = nums[curPosition]
    # print(f'{nums}')
sol = Solution()
nums = [1,2,3,4,5,6,7]
sol.rotate(nums, k = 3)
assert nums == [5,6,7,1,2,3,4]

nums = [1,2,3,4,5,6,7]
sol.rotate(nums, k = 2) 
assert nums == [6,7,1,2,3,4,5]

nums = [1,2,3,4,5,6,7]
sol.rotate(nums, k = 1) 
assert nums == [7,1,2,3,4,5,6]

nums = [1]
sol.rotate(nums, k = 2)
assert nums == [1]

nums = [1,2]
sol.rotate(nums, k = 2)
assert nums == [1,2]

nums = [1,2]
sol.rotate(nums, k = 1002)
assert nums == [1,2]

nums = [1,2]
sol.rotate(nums, k = 0)
assert nums == [1,2]

nums = [1,2]
sol.rotate(nums, k = 1)
assert nums == [2,1]

nums = [-1,-100,3,99]
sol.rotate(nums, k = 2)
assert nums == [3,99,-1,-100]
