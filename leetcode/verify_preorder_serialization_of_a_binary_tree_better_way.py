class Solution:
  '''
  Cannot solve it by myself :|
  '''
  def isValidSerialization(self, preorder: str) -> bool:
    arr = preorder.split(',')
    diff = 1
    for i in range(len(arr)):
      diff -= 1
      if diff < 0:
        return False
      if arr[i] != '#':
        diff += 2
    return diff == 0
sol = Solution()
assert sol.isValidSerialization("9,3,4,#,#,1,#,2,#,6,#,#") == False
assert sol.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#") == True
assert sol.isValidSerialization("9,3,#,#,#" ) == True
