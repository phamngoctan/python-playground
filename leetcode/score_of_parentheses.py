class Solution:
  def scoreOfParentheses(self, s: str) -> int:
    """ Keep cur variable as the score at current layer level
    What a smart solution!
    """
    stack = []
    cur = 0
    for ch in s:
      if ch == '(':
        stack.append(cur)
        cur = 0
      else:
        previousOperation = stack.pop()
        cur = previousOperation + max(cur * 2, 1)
    # print(f'{cur}')
    return cur

      
sol = Solution()
assert sol.scoreOfParentheses(s = "()") == 1
assert sol.scoreOfParentheses(s = "(())") == 2
assert sol.scoreOfParentheses(s = "()()") == 2
assert sol.scoreOfParentheses(s = "(()(()))") == 6
assert sol.scoreOfParentheses(s = "(((())))") == 8
