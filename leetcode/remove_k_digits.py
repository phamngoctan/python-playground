class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        2314 most significant order will be: 3 first, 2, 4, 1
        previous digit is greater than the current digit -> more significant OK
        """
        mStack = []
        for digit in num:
            while k > 0 and mStack and mStack[-1] > digit:
                mStack.pop() # remove the most significant digit when found one
                k -= 1
            mStack.append(digit)
        if k > 0: # this time, the stack already in increasing order
            mStack = mStack[:-k]
        ans = "".join(mStack)
        # remove the leading zero
        while ans and ans[0] == '0':
            ans = ans[1:]
        # print(f'{ans}')
        return ans if ans != "" else "0"

sol = Solution()
assert sol.removeKdigits("1432219", k = 3) == "1219"
assert sol.removeKdigits("10200", k = 1) == "200"
assert sol.removeKdigits("10200", k = 5) == "0"
