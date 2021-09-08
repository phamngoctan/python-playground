from typing import List

class Solution:
  def sort(self, arr:List):
    self.quick_sort(arr, 0, len(arr) - 1)

  def quick_sort(self, arr:List, left:int, right:int):
    if left < right:
      partitionIndex = self.partition(arr, left, right)
      self.quick_sort(arr, left, partitionIndex - 1)
      self.quick_sort(arr, partitionIndex + 1, right)

  def partition(self, arr:List, left:int, right:int):
    pivot = arr[right]
    partitionIndex = left
    for j in range(left, right):
      if arr[j] < pivot:
        self.swap(arr, partitionIndex, j)
        partitionIndex += 1
    self.swap(arr, partitionIndex, right)
    return partitionIndex

  def swap(self, arr, pos1, pos2):
    tmp = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = tmp

sol = Solution()
arr = [5,3,1,6,4,2]
sol.partition(arr, 0, len(arr) - 1)
# sol.sort(arr)
print(arr)


