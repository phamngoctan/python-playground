from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pDict = [0 for _ in range(26)]
        for c in p:
            pDict[ord(c) - ord('a')] += 1
        # print(f'{pDict}')
        curWindow = [0 for _ in range(26)]
        start = 0
        ans = []
        for end in range(len(s)):
            while end - start >= len(p):
                # print(f"{ord(s[start]) - ord('a')}")
                curWindow[ord(s[start]) - ord('a')] -= 1
                start += 1
            curWindow[ord(s[end]) - ord('a')] += 1
            if curWindow == pDict:
                ans.append(start)
            
            print(f'{curWindow}')
        return ans

sol = Solution()
assert sol.findAnagrams("cbaebabacd", p = "abc") == [0,6]
assert sol.findAnagrams("abab", "ab") == [0,1,2]