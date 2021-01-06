from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []
        operator = ["+", "-", "*", "/"]
        for i in tokens:
            print(i)
            if i in operator:
                res = int(stack.pop()) * int(stack.pop())
                stack.append(res)
            else:
                stack.append(i)
        return res

s = Solution()
print("Expect 9 and result is ", s.evalRPN(["2", "1", "+", "3", "*"]))
print("Expect 6 and result is ", s.evalRPN(["4", "13", "5", "/", "+"]))
print("Expect 22 and result is ", s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
