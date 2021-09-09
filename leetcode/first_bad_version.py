# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
def isBadVersion(version):
  return True if version >= 1 else False

class Solution:
  def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    left = 1
    right = n
    badVersion = None
    while left <= right:
      mid = (left + right) // 2
      if isBadVersion(mid):
        badVersion = mid
        right = mid - 1
      else:
        left = mid + 1
    return badVersion
      
        

sol = Solution()
print(f'{sol.firstBadVersion(9)}')
assert sol.firstBadVersion(9) == 1
assert sol.firstBadVersion(1) == 1