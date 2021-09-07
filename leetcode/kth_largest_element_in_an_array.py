from typing import List

class Solution:
  def findKthLargest(self, nums: List[int], k: int) -> int:
    return self.findKthLargestRecursively(nums, 0, len(nums) - 1, len(nums) - k)

  def findKthLargestRecursively(self, nums, left, right, k):
    if left <= right:
      partitionIndex = self.partition(nums, left, right)
      if partitionIndex == k:
        return nums[partitionIndex]
      elif partitionIndex < k:
        return self.findKthLargestRecursively(nums, partitionIndex + 1, right, k)
      else: 
        return self.findKthLargestRecursively(nums, left, partitionIndex - 1, k)

  def partition(self, nums, left, right):
    pivot = nums[right]
    partitionIndex = left
    for j in range(left, right): # right position will be excluded
      if nums[j] < pivot:
        self.swap(nums, j, partitionIndex)
        partitionIndex += 1
    self.swap(nums, partitionIndex, right)
    return partitionIndex
    
  def swap(self, nums, i, j):
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp

sol = Solution()
res = sol.findKthLargest([3,2,1,5,6,4], 2)
print(res)
assert res == 5

res = sol.findKthLargest([3],1)
assert res == 3

res = sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4)
assert res == 4
