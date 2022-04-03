class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Hash = [0] * 26
        for c in s1:
            s1Hash[ord(c) - ord('a')] += 1
        # print(f'{s1Hash}')
        # start = 0
        curHash = [0] * 26
        count = 0
        for end in range(len(s2)):
            curVal = ord(s2[end]) - ord('a')
            # if not s1Hash[curVal]:
            #     # curHash[ord(s2[end]) - ord('a')] += 1
            # # else:
            #     # print(f'current {end} {curHash}')
            #     while start < end:
            #         if curHash == s1Hash:
            #             return True
            #         curHash[ord(s2[start]) - ord('a')] -= 1
            #         start += 1
            curHash[curVal] += 1
            count += 1
            if count > len(s1):
                curHash[ord(s2[end - count + 1]) - ord('a')] -= 1
                count -= 1
            if curHash == s1Hash: 
                return True
        return False
sol = Solution()
assert sol.checkInclusion("abc", "cccccbabbbaaaa") == True
