arr = [1,2,3,4,5]
arr[0] = arr[0] - 1
print(arr)

arr[-1] += 4
print(arr)

arr[len(arr)//2] *= 2
print(arr)

for i in range(0, len(arr)):
    arr[i] += 3

print(arr)