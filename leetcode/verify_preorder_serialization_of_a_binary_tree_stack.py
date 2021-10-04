class Solution:
  '''
  Cannot solve it by myself :|
  '''
  def isValidSerialization(self, preorder: str) -> bool:
    arr = preorder.split(',')
    stack = []
    for i in range(len(arr)):
      while arr[i] == '#' and len(stack) > 0 and stack[-1] == '#':
        '''
        check stack emtpy to make sure the case where empty stack and the first element is #
        check the stack empty in case, the 9,#,#
        '''
        stack.pop()
        if not stack:
          return False
        stack.pop()
      stack.append(arr[i])
    # print(f'{stack}')
    return stack == ["#"]
    
sol = Solution()
assert sol.isValidSerialization("9,3,4,#,#,1,#,2,#,6,#,#") == False
assert sol.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#") == True
assert sol.isValidSerialization("9,3,#,#,#" ) == True
assert sol.isValidSerialization("9,#,#" ) == True
