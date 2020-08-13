n = int(input())
while (n != 0):
  arr = list(map(int, input().split()))[:n]
  stack = []
  i = 0
  count = 1;
  while (i < n):
    while (stack and stack[-1] == count):
        stack.pop()
        count += 1
    if (arr[i] != count):
      stack.append(arr[i])
    else:
      count += 1
    i += 1
  # print("count ", count)
  # print(stack)
  ok = True
  while (stack):
    # print (count, " vs ", stack[-1])
    if (count != stack.pop()):
      print("no")
      ok = False
      break;
    else:
      count += 1

  if (ok):
    print("yes")
  n = int(input())