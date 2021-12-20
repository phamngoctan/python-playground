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
        curNum = curNum*10 + int(char) #curNum*10 + 
      else:
        curStr += char
    # print(f'{curStr}')
    return curStr

  def decodeString_recursiveApproach(self, s: str) -> str:
    global i
    i = 0
    def helper(s):
      global i
      res = ""
      curNum = 0
      while i < len(s):
        c = s[i]
        i += 1
        if c == '[':
          sub = helper(s)
          res = res + curNum * sub
          curNum = 0 # reset the number after finishing the solving of sub problem
        elif c == ']':
          break # stop the loop for recursive call
        elif c.isnumeric():
          curNum = curNum*10 + int(c)
        else:
          res += c
      return res
    res = helper(s)
    # print(f'{res}')
    return res

sol = Solution()
assert sol.decodeString("10[LC]") == "LCLCLCLCLCLCLCLCLCLC"
assert sol.decodeString("3[2[a]]") == "aaaaaa"
assert sol.decodeString("3[a]2[bc]") == "aaabcbc"
assert sol.decodeString("3[a2[c]]") == "accaccacc"
assert sol.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
assert sol.decodeString("abc3[cd]xyz") == "abccdcdcdxyz"
assert sol.decodeString("3[z2[ab]]") == "zababzababzabab"
assert sol.decodeString("2[z2[ab]]cbd") == "zababzababcbd"
