class Solution:
  def isValid(self, s: str) -> bool:
    stack = []
    table = {
      ')' : '(',
      '}' : '{',
      ']' : '['
    }
    for char in s:
      if char in table:
        if not stack or stack.pop() != table[char]:
          return False
      else:
        stack.append(char)
    return len(stack) == 0

sol = Solution()
assert sol.isValid('{([])]') == False
assert sol.isValid('()[]{}') == True
assert sol.isValid('(]') == False
assert sol.isValid('([)]') == False
assert sol.isValid('{[]}') == True
assert sol.isValid('') == True
assert sol.isValid(')') == False
assert sol.isValid('{') == False
assert sol.isValid('{{{{{') == False
assert sol.isValid('{{{{{}}}}}}') == False