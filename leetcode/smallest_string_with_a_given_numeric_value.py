class Solution:
    def getSmallestString_fromSuggestion(self, n: int, k: int) -> str:
        """This solution idea is good but not efficient.
        It can run in O(n) while the idea is that
        we just need to cover all the Z characters and one remaining
            value of min(k, 25)
        """
        ans = ""
        while k > 0:
            maxCur = k - (n - 1)
            if maxCur >= 26:
                ans = "z" + ans
                k -= 26
            else:
                ans = chr(ord('a') - 1 + maxCur) + ans
                k -= maxCur
            n -= 1
        return ans
        # print(f"current answer: {ans} remaining k: {k} remaining n {n}")
        # n = 3 => max = 3 * 26 = 78
        
        # n = 3, k = 27 => n = 2, 2 * 1 = 2, => ans += "y"
        # n = 2, k = 2 => n = 1, 1 * 1 = 1 => ans += "a"
        # n = 1, k = 1 => n = 0, ans += "a"
        
        # n = 5, k = 73, n = 4, 4 * 1 = 4, 73 - 4 >= 26 => ans += "z"
        # n = 4, k = 47, n = 3, 3 * 1 = 3, 73 - 3 >= 26 => ans += "z"
        # n = 3, k = 21, n = 2, 2 * 1 = 2, 21 - 2 >= 26? => ans += 'a' + 19
        # n = 2, k = 2,  n = 1, 1 * 1 = 1, 2 - 1  >= 26? => ans += 'a' + 0

    def getSmallestString(self, n: int, k: int) -> str:
        ans = []
        for _ in range(n):
            ans.append("a") # ans += "a" # also fine
        k = k - n
        for i in range(n - 1, -1, -1):
            if k > 0:
                ans[i] = chr(ord(ans[i]) + min(k, 25))
                k -= min(k, 25)
            else:
                break
        return "".join(ans)


