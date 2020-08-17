import queue

Q = int(input())


dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def BFS(graph, s, e):
  q = queue.Queue()
  # visited = [[False] * N] * M
  visited = [[False] * M for i in range(N)]
  q.put(s)
  visited[s[0]][s[1]] = True
  # print(s[0], s[1])
  # print(visited)
  
  while not q.empty():
    cur = q.get()
    # print(cur)
    for i in range (4):
      x = cur[0] + dir[i][0]
      y = cur[1] + dir[i][1]
      # print(x, y)
      if (x == e[0] and y == e[1]):
        return True
      # if (x == 2 and y == 1):
      #     print(graph[x][y])
      #     print(visited[x][y])
      if (x >= 0 and x < N and y >= 0 and y < M and not visited[x][y] and graph[x][y] == '.') :
        visited[x][y] = True
        q.put([x, y])
        # if (x == 2 and y == 1):
        #   print('putted [2, 1]')
    # print(visited)
  return False


def validate(graph) :
  points = []
  count = 0
  for i in range (N):
    for j in range (M):
      if (graph[i][j] == '.'
        and (i == 0 or i == N - 1 or j == 0 or j == M - 1)):
        count += 1
        points.append([i, j])
  
  if (count != 2):
    print('invalid')
  else:
    res = BFS(graph, points[0], points[1])
    print('valid' if res else 'invalid')

for query in range(Q):
  N, M = map(int, input().split())
  graph = [] * N
  for i in range (N):
    graph.append(list(input()))
  validate(graph)
