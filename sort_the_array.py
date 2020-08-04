import sys

n = int(input())
arr = list(map(int, input().split()))[:n]

arr_1 = list.copy(arr)
arr_1.sort()
first = -1
for i in range(n):
	if (arr[i] != arr_1[i]):
		first = i
		break

if (first == -1):
	print("yes")
	print("1 1")
	sys.exit()

second = -1
for i in range(n - 1, i, -1):
	if (arr[i] != arr_1[i]):
		second = i
		break

i = first
j = second
while (i < j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp
	i += 1
	j -= 1

if (arr == arr_1):
	print("yes")
	print(first + 1, second + 1)
else:
	print("no")
