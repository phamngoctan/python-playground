k = int(input())
arr = list(map(int, input().split()))[:12]

arr_1 = sorted(arr, reverse=True)

fre = 1005 * [0]
count = 0

i = 0

while(k>0 and i < 12):
  k = k - arr_1[i]
  i +=1
  count += 1

if(i < 12 or k == 0):
  print(count)
else:
  print(-1)
