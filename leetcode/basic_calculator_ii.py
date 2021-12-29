class Solution:
  def calculate(self, s: str) -> int:
    stack = []
    s = s.strip()
    cur = 0
    previousOperation = '+'
    for i in range(len(s)):
      if s[i].isdigit():
        cur = cur * 10 + ord(s[i]) - ord('0')
      if (not s[i].isdigit() and s[i] != ' ') or i == len(s) - 1:
        if previousOperation == '*':
          cur = cur*stack.pop()
          stack.append(cur)
        elif previousOperation == '/':
          cur = int(stack.pop()/cur) # in case -3/2 (expected: -1 instead of -3//2 = -2)
          stack.append(cur)
        elif previousOperation == '+':
          stack.append(cur)
        elif previousOperation == '-':
          stack.append(-cur)
        previousOperation = s[i]
        cur = 0
    ans = sum(stack)
    # print(f'{ans}')
    return ans

sol = Solution()
assert sol.calculate(s = "14-3/2") == 13
assert sol.calculate(s = "42") == 42
assert sol.calculate(s = "2*2+5") == 9
assert sol.calculate(s = "3+2*2*3*4") == 51
assert sol.calculate(s = "3+2*2") == 7
assert sol.calculate(s = " 3/2 ") == 1
assert sol.calculate(s = " 3+5 / 2 ") == 5
