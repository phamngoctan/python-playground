from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        dict = {}
        dict[')'] = '('
        dict[']'] = '['
        dict['}'] = '{'
        stack = []
        for i in s:
            if i in dict:
                if len(stack) == 0 or stack[-1] != dict.get(i):
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0

s = Solution()
print("expect True and result is ", s.isValid("()"))
print("expect True and result is ", s.isValid("()[]{}"))
print("expect False and result is ", s.isValid("(]"))
print("expect False and result is ", s.isValid("([)]"))
print("expect True and result is ", s.isValid("{[]}"))
print("expect False and result is ", s.isValid("["))