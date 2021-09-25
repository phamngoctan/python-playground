from typing import List

class Solution:
  def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) <= 1:
      return
    def quickSort(nums, start, end):
      if start < end:
        partitionIndex = partition(nums, start, end)
        quickSort(nums, start, partitionIndex - 1)
        quickSort(nums, partitionIndex + 1, end)
      # print(f'{nums}')

    def partition(nums, start, end):
      pivot = nums[end]
      i = start
      # print(f'{start}, {end}')
      for j in range(start, end):
        if nums[j] < pivot:
          swap(nums, i, j)
          i += 1
      swap(nums, i, end)
      return i
    def swap(nums, i, j):
      tmp = nums[i]
      nums[i] =nums[j]
      nums[j] = tmp
    quickSort(nums, 0, len(nums) - 1)
sol = Solution()
nums = [2,0,2,1,1,0]
sol.sortColors(nums)
assert nums == [0,0,1,1,2,2]

nums = [2,0,1]
sol.sortColors(nums)
assert nums == [0,1,2]

nums = [0]
sol.sortColors(nums)
assert nums == [0]

nums = [1]
sol.sortColors(nums)
assert nums == [1]
