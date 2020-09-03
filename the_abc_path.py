direction = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

def isValid(graph, x, y):
  return x >= 0 and x < R and y >= 0 and y < C

def DFS(graph, s):
  x = s[0]
  y = s[1]
  m = 0
  visited[x][y] = True
  for i in range(8):
    newX = x + direction[i][0]
    newY = y + direction[i][1]
    if (isValid(graph, newX, newY) and not visited[newX][newY] and ord(graph[newX][newY]) - ord(graph[x][y]) == 1):
      m = max(DFS(graph, [newX, newY]), m)
  m += 1
  return m
  
    

R, C = map(int, input().split())
case = 1
while (R != 0 and C != 0):
  graph = []
  for i in range(R):
    graph.append(list(input()))

  maxRes = 0
  for i in range(R):
    for j in range(C):
      visited = [[False] * C for i in range(R)]
      if (graph[i][j] == 'A'):
        maxRes = max(maxRes, DFS(graph, [i, j]))
  print("Case ", case, ": ", maxRes, sep='')
  case += 1
  R, C = map(int, input().split())
