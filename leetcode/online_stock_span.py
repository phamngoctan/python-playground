class StockSpanner:
  def __init__(self):
    # self.dict = {}
    MAX_VALUE = 10**5 + 1
    self.stack = [[MAX_VALUE, 0]]
    self.currentPosition = 0

  def next(self, price: int) -> int:
    self.currentPosition += 1
    while len(self.stack) > 0 and self.stack[-1][0] <= price:
      self.stack.pop()
    if len(self.stack) > 0:
      biggerStock = self.stack[-1]
    self.stack.append([price, self.currentPosition])
    res = self.currentPosition - biggerStock[1]
    # print(f'{res}')
    return res
# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
# assert obj.next(100) == 1
# assert obj.next(80) == 1
# assert obj.next(60) == 1
# assert obj.next(70) == 2
# assert obj.next(60) == 1
# assert obj.next(75) == 4
# assert obj.next(85) == 6

# assert obj.next(31) == 1
# assert obj.next(41) == 2
# assert obj.next(48) == 3
# assert obj.next(59) == 4
# assert obj.next(71) == 5

assert obj.next(28) == 1
assert obj.next(14) == 1
assert obj.next(28) == 3
assert obj.next(35) == 4