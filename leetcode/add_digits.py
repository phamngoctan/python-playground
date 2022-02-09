class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            strOfNum = str(num)
            tmp = 0
            for c in strOfNum:
                tmp += int(c)
            num = tmp
        # print(f'{num}')
        return num

    def addDigits_superIdea(self, num: int) -> int:
        """Super idea from LC"""
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9
sol = Solution()
assert sol.addDigits(38) == 2
assert sol.addDigits(1) == 1
assert sol.addDigits(0) == 0
assert sol.addDigits(1111) == 4
