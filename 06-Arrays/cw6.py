#numpy biblioteka

arr=[2,3,7,5,4]
#a
print("array", arr)
#b
print("length", len(arr))
#c
print(arr[0])
#d
print(arr[1])
#e
print(arr[-1])
#f
print(arr[-2])
#g
print(arr[0] + arr[-1])
#h
print(arr[int(len(arr)//2)])
#i
for i in range(0, len(arr)):
    print(arr[i], end=" ")
#j
for i in range(0, len(arr)//2 + 1):
    print(arr[i], end=" ")



