class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        """
        Borrow the idea from Mr. Lee LC
        """
        ans = 0
        while target > startValue: # // 2 until target smaller than the startValue
            target = target // 2 if target % 2 == 0 else target + 1
            ans += 1
        return ans + (startValue - target)
    
    def brokenCalc_TLE(self, startValue: int, target: int) -> int:
        """BFS will not work as this is the greedy problem. TLE happened.
        """
        def bfs(startValue, target):
            queue = [startValue]
            visited = set()
            visited.add(startValue)
            operation = 0
            while len(queue) > 0:
                curLength = len(queue)
                for _ in range(curLength):
                    cur = queue.pop(0)
                    if cur == target:
                        return operation
                    if not cur * 2 in visited:
                        queue.append(cur*2)
                        visited.add(cur*2)
                    if not cur - 1 in visited:
                        queue.append(cur - 1)
                        visited.add(cur - 1)
                operation += 1
        return bfs(startValue, target)