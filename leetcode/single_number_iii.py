from typing import List, Mapping

class Solution:
  '''
  # this bit has value one will be the diff between a and b. Only one of them has this bit set
  # Next step, find all nums that have this bit set. a will be in there by xor operator again all of it.
  # To find b, a xor aXorB || 
  #   or another way, collect all nums that has no right most bit set => xor all nums again
  '''
  def singleNumber(self, nums: List[int]) -> List[int]:
    aXorB = 0
    for num in nums:
      aXorB ^= num
    # print('{0:b}'.format(aXorB))
    # print('{0:b}'.format(-aXorB))
    rightMostBit = aXorB & -aXorB
    '''
    # bu 2 - second complement: for negative number, it reverses all the bit and plus 1 to the result.
    # that's why the above code can find out the right most bit set
    '''
    a = 0
    for num in nums:
      if (rightMostBit & num) != 0:
        a ^= num
    return [a, a ^ aXorB]

# print(f'{3 ^ 5 ^ 1 ^ 2 ^ 1 ^ 2}')
# print('{0:b}'.format(6))
# print('{0:b}'.format(-6))
# print('{0:b}'.format(6&-6))
sol = Solution()
assert sol.singleNumber([1,2,1,3,2,5]) == [3,5]
