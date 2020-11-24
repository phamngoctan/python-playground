
class Solution:
    def isHappy(self, n: int) -> bool:
        freq = []
        while True:
            if n in freq:
                print(freq)
                print(n)
                return False
            freq.append(n)
            cur = 0
            for d in str(n):
                cur = cur + pow(int(d), 2)
            if cur == 1:
                return True
            n = cur
            
s = Solution()
print(s.isHappy(19))
print(s.isHappy(2))