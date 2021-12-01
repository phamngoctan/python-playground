MAX = 20
parent = []
def makeSet():
  global parent
  parent = [i for i in range(MAX + 5)]
def findSet(u):
  while u != parent[u]:
    u = parent[u]
  return u # parent = None
def unionSet(u, v):
  uParent = findSet(u)
  vParent = findSet(v)
  # at this point, just randomly put the second 
  # as the parent of first param
  parent[uParent] = vParent

'''
Sample input
9
1 2 1
2 3 1
4 5 1
5 6 1
2 6 2
6 7 1
7 3 1
6 2 2
7 1 2
'''
if __name__ == '__main__':
  Q = int(input())
  makeSet()
  for i in range(Q):
    u, v, query = map(int, input().split())
    if query == 1:
      unionSet(u, v)
    elif query == 2:
      parentU = findSet(u)
      parentV = findSet(v)
      if parentU == parentV:
        print("YES")
      else:
        print("NO")
    