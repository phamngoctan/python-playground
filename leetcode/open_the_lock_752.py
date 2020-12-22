from typing import List
from queue import Queue

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        startLock = "0000"
        if startLock in deadends:
            return -1

        dic = {}
        dic[startLock] = 0
        queue = Queue()
        start = [0,0,0,0]
        queue.put(start)
        while not queue.empty():
            cur = queue.get()
            curLock = ''.join(map(str, cur))
            if ''.join(map(str, cur)) == target:
                return dic[curLock]
            for i in range(4):
                down = []
                up = []
                for j in range(4):
                    if i == j:
                        down.append((cur[j] - 1 + 10) % 10)
                        up.append((cur[j] + 1 + 10) % 10)
                    else:
                        down.append(cur[j])
                        up.append(cur[j])
                downLock = ''.join(map(str, down))
                upLock = ''.join(map(str, up))

                if downLock not in deadends \
                        and downLock not in dic:
                    dic[downLock] = dic[curLock] + 1
                    queue.put(down)
                if upLock not in deadends \
                        and upLock not in dic:
                    dic[upLock] = dic[curLock] + 1
                    queue.put(up)
        return -1


s = Solution()

deadEnds = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
print(s.openLock(deadEnds, target))

deadEnds = ["8888"]
target = "0009"
print(s.openLock(deadEnds, target))

deadEnds = ["0000"]
target = "8888"
print(s.openLock(deadEnds, target))

deadEnds = ["8887","8889","8878","8898","8788","8988","7888","9888"]
target = "8888"
print(s.openLock(deadEnds, target))

print("#################")
print("Testing Python stuff")
print(str([0,0,0,0]))
print(''.join(map(str, [0,0,1,2])))

testDic = {}
testDic["0000"] = 0
print("1000" not in testDic)