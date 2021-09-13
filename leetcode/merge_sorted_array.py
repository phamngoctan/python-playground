from typing import List

class Solution:
  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = 0
    j = 0
    newArr = []
    while i < m and j < n:
      # print(f'{i} and {j}')
      if nums1[i] < nums2[j]:
        newArr.append(nums1[i])
        i += 1
      else:
        newArr.append(nums2[j])
        j += 1
    while i < m:
      newArr.append(nums1[i])
      i += 1
    while j < n:
      newArr.append(nums2[j])
      j += 1
    
    for i in range(len(nums1)):
      nums1[i] = newArr[i]


sol = Solution()
nums1 = [1,2,3,0,0,0]
sol.merge(nums1, 3, [2,5,6], 3)
assert nums1 == [1,2,2,3,5,6]
nums1 = [1,5,7,0,0,0]
sol.merge(nums1, 3, [3,5,6], 3)
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
      