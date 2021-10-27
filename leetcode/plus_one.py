from typing import List

class Solution:
  def plusOne(self, digits: List[int]) -> List[int]:
    strRes = str(int(''.join(str(x) for x in digits)) + 1)
    # print(f'{list(map(int, strRes))}')
    return list(int(s) for s in strRes)

sol = Solution()
assert sol.plusOne([1,2,3]) == [1,2,4]
assert sol.plusOne([4,3,2,9]) == [4,3,3,0]
assert sol.plusOne([9,9,9,9]) == [1,0,0,0,0]
