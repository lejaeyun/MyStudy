import sys
input = sys.stdin.readline

arr = list()
for _ in range(5) :
    arr.append(int(input()))

result = list()
for i in range(3) :
    for j in range(3,5) :
        result.append(arr[i]+arr[j] - 50)

print(min(result))
