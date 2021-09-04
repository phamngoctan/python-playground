class Solution:
  def isValid(self, s: str) -> bool:
    count = 0
    stack = []
    input = {}
    input[')'] = '('
    input['}'] = '{'
    input[']'] = '['
    while count < len(s):
      if s[count] in input:
        if not stack or stack.pop() != input[s[count]]:
          return False
      else:
        stack.append(s[count])
      count += 1
    return True if len(stack) == 0 else False

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