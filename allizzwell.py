direction = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
sentence = list('ALLIZZWELL')

def isInvalid(x, y):
  return x< 0 or x > R-1 or y<0 or y>C-1 

def DFS(graph, start, count):
  x1 = start[0]
  y1 = start[1]
  global found
  if(count == len(sentence)):
    found = True
    return

  for i in range(8):
    x2 = x1 + direction[i][0]
    y2 = y1 + direction[i][1]
    # print(count)
    if(isInvalid(x2, y2) or graph[x2][y2] != sentence[count] or v[x2][y2]):
      continue
    v[x2][y2] = True
    DFS(graph, [x2, y2], count + 1)
    v[x2][y2] = False

def findAllMatchedPosition(line, curX, char):
  index = 0
  res = []
  while index < len(line):
    index = line.find(char, index)
    if index == -1:
      break
    res.append([curX, index])
    index = index + len(char)
  return res

def runOneCase():
  for i in range(R):
    line = input()
    graph.append(list(line))
    s.extend(findAllMatchedPosition(line, i, 'A'))

  # print(s)
  for i in range(len(s)):
    if not found:
      DFS(graph, s[i], 1)
  print("YES" if found else "NO")
  input()
  
t = int(input())
for case in range(t):
  R, C = map(int, input().split())
  v = [[False] * C for i in range(R)]
  graph = []
  s = []
  found = False
  runOneCase()