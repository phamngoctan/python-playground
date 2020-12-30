class Solution:
    def numSquares(self, n: int) -> int:
        if n < 2:
            return n

        d = 1
        squares = []
        while d * d <= n:
            squares.append(d * d)
            d += 1

        q = set()
        q.add(n)
        count = 0
        while q:
            count += 1
            temp = set()
            for x in q:
                for y in squares:
                    if x == y:
                        return count
                    if x < y:
                        break
                    temp.add(x - y)
            q = temp
        return count

s = Solution()
# print("Value ", s.numSquares(12), " should be 3")
print("Value ", s.numSquares(6175), " should be 4")

'''
For the time complexity: would it be n²?

The depth of the BFS is at most 4 by the four-square theorem (every natural number can be represented as the sum of four integer squares)
At every dept there will be at most sqrt(n) children, because there's at most sqrt(n) perfect squares that are smaller than n

Therefore, (sqrt(n))^4 = n²
'''