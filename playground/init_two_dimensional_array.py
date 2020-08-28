# init 3x3 dimensional array
# wrong approach
# arr = [[0] * 3] * 3
arr = [[0] * 3 for i in range(3)] 
arr[0][0] = 1
print(arr)
