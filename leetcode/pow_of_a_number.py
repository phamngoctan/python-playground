class Solution:
    # naive approach

    # def myPow(self, x: float, n: int) -> float:
    #     return round(self.__myPowWithoutRound(x, n), 5)
    # def __myPowWithoutRound(self, x: float, n: int) -> float:
    #     if n == 0:
    #         return 1
    #     if n == 1:
    #         return x
    #     if n < 0:
    #         val = self.__myPowWithoutRound(x, n * (-1))
    #         # print(val)
    #         return 1 / val
    #     else:
    #         val = self.__myPowWithoutRound(x, n - 1)
    #         # print(val)
    #         return x * val

    def myPow(self, x: float, n: int) -> float:
        if abs(x) < 1e-40:
            return 0
        if n == 0:
            return 1
        if n < 0:
            # return 1 / self.myPow(x, -n)
            return self.myPow(1/x, -n)
        partOfPow = self.myPow(x, n//2)
        if n % 2 == 0:
            return partOfPow * partOfPow
        if n % 2 == 1:
            return partOfPow * partOfPow * x

s = Solution()
print("x is O (should print 1) ", s.myPow(0, 0))
print("x is 1 (should print 1) ", s.myPow(1, 0))
print("case 3 (should print 2) ", s.myPow(2, 1))
print("case 4 (should print 0.5) ", s.myPow(2, -1))
print("case 5 (should print 0.25) ", s.myPow(2, -2))
print("case 6 (should print -8) ", s.myPow(-2, 3))
print("case 7 (should print -0.125) ", s.myPow(-2, -3))
print("case 8 (should print 9.26100) ", s.myPow(2.1, 3))
print("case 9 (should print 700.28148) ", s.myPow(8.88023, 3))
print("case 10 (should print 700.28148) ", s.myPow(0.00001, 2147483647))

print(10.5 // 2)
print(10.5 / 2)