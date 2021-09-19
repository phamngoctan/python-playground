from typing import List
from collections import Counter

class Solution:
  def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
    visited = [False for i in range(len(watchedVideos))]
    queue = [id]
    visited[id] = True
    count = 0
    videos = []
    while queue and count < level:
      curQueueSize = len(queue)
      for _ in range(curQueueSize):
        cur = queue.pop(0)
        # print(f'count {count}: {cur}')
        curFriends = friends[cur]

        for curFriend in curFriends:
          if not visited[curFriend]:
            if count == level - 1:
              videos.extend(watchedVideos[curFriend])
            visited[curFriend] = True
            queue.append(curFriend)
      count += 1
    # print(f'{Counter(videos)}')

    # -item[1] if decreasing order or frequency
    # Counter({'C': 2, 'B': 1})
    single_occurrences = sorted(Counter(videos).items(), key=lambda item: (item[1], item[0])) 
    res = list(map(lambda i: i[0], single_occurrences))
    
    # print(res)
    return res
sol = Solution()
sol.watchedVideosByFriends(watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 1) == ["B","C"]
sol.watchedVideosByFriends([["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 2) == ["D"]
sol.watchedVideosByFriends([["A"],["C"]], friends = [[1],[0]], id = 0, level = 1) == ["C"]
sol.watchedVideosByFriends([["A"],["C"]], friends = [[1],[0]], id = 1, level = 1) == ["A"]
sol.watchedVideosByFriends([["A"],["C"]], friends = [[],[]], id = 1, level = 1) == []
