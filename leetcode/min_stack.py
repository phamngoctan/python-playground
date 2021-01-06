
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.internalStorage = []
    def push(self, x: int) -> None:
        minVal = x
        if len(self.internalStorage) > 0:
            minVal = min(self.internalStorage[-1][1], x)
        self.internalStorage.append([x, minVal])

    def pop(self) -> None:
        self.internalStorage.pop()

    def top(self) -> int:
        return self.internalStorage[-1][0]

    def getMin(self) -> int:
        return self.internalStorage[-1][1]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
print(obj.pop())
obj.push(1)
param_3 = obj.top()
param_4 = obj.getMin()