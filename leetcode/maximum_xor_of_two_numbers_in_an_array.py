from typing import List

class Solution:
  def findMaximumXOR1(self, nums: List[int]) -> int:
    maxVal = max(nums)
    firstInnerZeroPosition = 0
    valAtFirstInnerZeroPosition = 0
    tmp = maxVal
    i = 0
    strBinary = ''
    while tmp != 0:
      if tmp % 2 == 0:
        firstInnerZeroPosition = i
        valAtFirstInnerZeroPosition = 0 if not strBinary else int(strBinary, 2)
      strBinary = str(tmp%2) + strBinary
      tmp = tmp // 2
      i += 1
    print(f'{valAtFirstInnerZeroPosition}')
    print(f'{strBinary}')
    maxAllowedValue = 2 ** (firstInnerZeroPosition + 1) - 1
    print(f'{maxAllowedValue}')
    
    maxXor = -1
    for num in nums:
      if num < maxAllowedValue:
        maxXor = max(maxXor, valAtFirstInnerZeroPosition ^ num)
    ans = (maxVal - valAtFirstInnerZeroPosition) + maxXor
    print(f'{ans}')
    return ans

  def findMaximumXOR(self, nums: List[int]) -> int:
    """Bruceforce"""
    ans = -1
    for i in range(len(nums)):
      for j in range(i + 1, len(nums)):
        ans = max(ans, nums[i] ^ nums[j])
        if nums[i] ^ nums[j] == 127:
          print(f'{nums[i]} ^ {nums[j]}')
    print(f'{ans}')
    return ans

sol = Solution()
# assert sol.findMaximumXOR([3,10,5,25,2,8]) == 28
assert sol.findMaximumXOR([14,70,53,83,49,91,36,80,92,51,66,70]) == 127
