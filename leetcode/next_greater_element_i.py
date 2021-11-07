from typing import List

class Solution:
  def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    monotoneStack = []
    dict = {}
    for num in nums2:
      while len(monotoneStack) > 0 and monotoneStack[-1] < num:
        dict[monotoneStack.pop()] = num
      monotoneStack.append(num)
    # print(f'{dict}')
    res = []
    for num in nums1:
      res.append(dict.get(num, -1))
    return res
sol = Solution()
assert sol.nextGreaterElement([4,1,2], nums2 = [1,3,4,2]) == [-1,3,-1]
assert sol.nextGreaterElement([1,2,4], nums2 = [2,3,1,4]) == [4,3,-1]