from typing import List
import random

class Solution:
  def sortArray(self, nums: List[int]) -> List[int]:
    def quickSort(nums, s, e):
      if s < e:
        partitionIndex = partition(nums, s, e)
        quickSort(nums, s, partitionIndex - 1)
        quickSort(nums, partitionIndex + 1, e)
    def partition(nums, s, e):
      pivot = nums[e]
      partitionIndex = s
      for j in range(s, e + 1):
        if nums[j] < pivot:
          swap(nums, partitionIndex, j)
          partitionIndex += 1
      swap(nums, partitionIndex, e)
      return partitionIndex
    def swap(nums, i, j):
      if i != j:
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
    random.shuffle(nums)
    quickSort(nums, 0, len(nums) - 1)
    return nums
sol = Solution()
assert sol.sortArray([5,2,3,1]) == [1,2,3,5]
assert sol.sortArray([5,1,1,2,0,0]) == [0,0,1,1,2,5]
assert sol.sortArray([1,7,4,3,5,2]) == [1,2,3,4,5,7]
assert sol.sortArray([1]) == [1]
assert sol.sortArray([1, -2]) == [-2, 1]
