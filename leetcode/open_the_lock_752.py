from typing import List
from queue import Queue

class Solution:
    def openLockNaive(self, deadends: List[str], target: str) -> int:
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
                    print("put ", downLock, " to the queue")
                if upLock not in deadends \
                        and upLock not in dic:
                    dic[upLock] = dic[curLock] + 1
                    queue.put(up)
                    print("put ", upLock, " to the queue")
        return -1

    #TODO: improve it
    def openLock(self, deadends: List[str], target: str) -> int:
        startLock = "0000"
        if startLock in deadends:
            return -1

        # visited = []
        # visited.extend(deadends)
        visited = set(deadends)
        count = -1
        queue = Queue()
        start = [0, 0, 0, 0]
        queue.put(start)
        while not queue.empty():
            count = count + 1
            curQueueSize = queue.qsize()
            for i in range(curQueueSize):
                cur = queue.get()
                if ''.join(map(str, cur)) == target:
                    return count
                relatedLocks = self.getRelatedLock(list(map(int, cur)))
                for relatedLock in relatedLocks:
                    if relatedLock not in visited:
                        queue.put(relatedLock)
                        visited.add(relatedLock)
                        # print("put ", relatedLock, " to the queue")
        return -1

    def getRelatedLock(self, cur) -> List:
        relatedLocks = []
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
            relatedLocks.append(''.join(map(str, down)))
            relatedLocks.append(''.join(map(str, up)))
        return relatedLocks


s = Solution()

# print("#################")
# deadEnds = ["0201", "0101", "0102", "1212", "2002"]
# target = "0202"
# print(s.openLock(deadEnds, target))
#
# deadEnds = ["8888"]
# target = "0009"
# print(s.openLock(deadEnds, target))
#
# deadEnds = ["0000"]
# target = "8888"
# print(s.openLock(deadEnds, target))

deadEnds = ["8887","8889","8878","8898","8788","8988","7888","9888"]
target = "8888"
print(s.openLock(deadEnds, target))

deadEnds = ["0201","0101","0102","1212","2002"]
target = "0000"
print(s.openLock(deadEnds, target))
#
# print("#################")
# deadEnds = ["0201", "0101", "0102", "1212", "2002"]
# target = "0202"
# print(s.openLockNaive(deadEnds, target))
#
# deadEnds = ["8888"]
# target = "0009"
# print(s.openLockNaive(deadEnds, target))
#
# deadEnds = ["0000"]
# target = "8888"
# print(s.openLockNaive(deadEnds, target))
#
# deadEnds = ["8887","8889","8878","8898","8788","8988","7888","9888"]
# target = "8888"
# print(s.openLockNaive(deadEnds, target))

# print("#################")
# print("Testing Python stuff")
# print(str([0,0,0,0]))
# print(''.join(map(str, [0,0,1,2])))

# testDic = {}
# testDic["0000"] = 0
# print("1000" not in testDic)

# testList = ["8209", "8201"]
# print("0000" not in testList)
#
# src = "0000"
# print(enumerate(src))
# for i, ch in enumerate(src):
#     num = int(ch)
#     print(src[:i] + str((num - 1) % 10) + src[i + 1:])