from typing import List

class Solution:
  def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
    h1 = [False for i in range(101)]
    for num in nums1:
      if not h1[num]:
        h1[num] = True
    h2 = [False for i in range(101)]
    for num in nums2:
      if not h2[num]:
        h2[num] = True
    h3 = [False for i in range(101)]
    for num in nums3:
      if not h3[num]:
        h3[num] = True
    res = []
    for i in range(1,101):
      count = 0
      count += 1 if h1[i] else 0
      count += 1 if h2[i] else 0
      count += 1 if h3[i] else 0
      if count >= 2:
        res.append(i)
    # print(f'{res}')
    return res
sol = Solution()
assert sorted(sol.twoOutOfThree(nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3])) == [2,3]
assert sorted(sol.twoOutOfThree(nums1 = [3,1], nums2 = [2,3], nums3 = [1,2])) == [1,2,3]
assert sorted(sol.twoOutOfThree(nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5])) == []
assert sorted(sol.twoOutOfThree(nums1 = [1], nums2 = [], nums3 = [])) == []
