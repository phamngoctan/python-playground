from typing import List

class Solution:
  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = m - 1
    j = n - 1
    tail = len(nums1) - 1
    while i >= 0 and j >= 0:
      # print(f'{i} and {j}')
      if nums1[i] > nums2[j]:
        nums1[tail] = nums1[i]
        i -= 1
      else:
        nums1[tail] = nums2[j]
        j -= 1
      tail -= 1
    while i >= 0:
      nums1[tail] = nums1[i]
      i -= 1
      tail -= 1
    while j >= 0:
      nums1[tail] = nums2[j]
      j -= 1
      tail -= 1

sol = Solution()
nums1 = [1,2,3,0,0,0]
sol.merge(nums1, 3, [2,5,6], 3)
# print(f'{nums1}')
assert nums1 == [1,2,2,3,5,6]
nums1 = [1,5,7,0,0,0]
sol.merge(nums1, 3, [3,5,6], 3)
# print(f'{nums1}')
assert nums1 == [1,3,5,5,6,7]
nums1 = [1,1,1,0,0,0]
sol.merge(nums1, 3, [3,5,6], 3)
assert nums1 == [1,1,1,3,5,6]
nums1 = [0]
sol.merge(nums1, 0, [1], 1)
assert nums1 == [1]
nums1 = [1]
sol.merge(nums1, 1, [], 0)
assert nums1 == [1]
# print(f'{nums1}')
      