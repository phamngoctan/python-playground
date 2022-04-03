class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """Using one variable to store the difference"""
        diff = ord(t[-1])
        for i in range(len(s)):
            diff -= ord(s[i])
            diff += ord(t[i])
        return chr(diff)

    def findTheDifference_xor(self, s: str, t: str) -> str:
        """Using XOR operator"""
        ans = ord(t[-1])
        for i in range(len(s)):
            ans ^= ord(s[i])
            ans ^= ord(t[i])
        return chr(ans)

    def findTheDifference_hash(self, s: str, t: str) -> str:
        """My idea"""
        arr = [0] * 26
        for c in s:
            arr[ord(c) - ord('a')] += 1
        for c in t:
            arr[ord(c) - ord('a')] -= 1
        for i, val in enumerate(arr):
            if val != 0:
                return chr(ord('a') + i)

sol = Solution()
assert sol.findTheDifference(s = "abcd", t = "abcde") == "e"
assert sol.findTheDifference(s = "", t = "y") == "y"
