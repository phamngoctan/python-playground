class Solution:
  def decodeString(self, s: str) -> str:
    curStr = ''
    curNum = 0
    stack = []
    for char in s:
      if char == '[':
        stack.append(curStr)
        stack.append(curNum)
        curNum = 0
        curStr = ''
      elif char == ']':
        previousNum = stack.pop()
        previousStr = stack.pop()
        curStr = previousStr + curStr*previousNum
      elif char.isnumeric():
        curNum = curNum*10 + int(char)
      else:
        curStr += char
    # print(f'{curStr}')
    return curStr

sol = Solution()
assert sol.decodeString("3[a]2[bc]") == "aaabcbc"
assert sol.decodeString("3[a2[c]]") == "accaccacc"
assert sol.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
assert sol.decodeString("abc3[cd]xyz") == "abccdcdcdxyz"
assert sol.decodeString("3[z2[ab]]") == "zababzababzabab"
assert sol.decodeString("2[z2[ab]]cbd") == "zababzababcbd"
