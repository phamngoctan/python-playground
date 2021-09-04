class Solution:
  def minRemoveToMakeValid(self, s: str) -> str:
    deletedPosition = []
    stack = []
    for index, char in enumerate(s):
      # print(f'{char} => {index}')
      if char == '(':
        stack.append(index)
      elif char == ')':
        if stack:
          stack.pop()
        else:
          deletedPosition.append(index)
    
    while stack:
      deletedPosition.append(stack.pop())
    
    # print(deletedPosition)
    res = []
    for index, char in enumerate(s):
      if not index in deletedPosition:
        res.append(char)
    return ''.join(res)
  
sol = Solution()
assert sol.minRemoveToMakeValid('a)b(c)d') == 'ab(c)d'
assert sol.minRemoveToMakeValid('))((') == ''
assert sol.minRemoveToMakeValid('(a(b(c)d)') == 'a(b(c)d)'
assert sol.minRemoveToMakeValid('lee(t(c)o)de)') == 'lee(t(c)o)de'
assert sol.minRemoveToMakeValid('leetcode()') == 'leetcode()'

