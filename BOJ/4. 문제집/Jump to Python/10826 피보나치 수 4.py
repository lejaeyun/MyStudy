import sys
input = sys.stdin.readline

arr = [0,1]
n = int(input())
for i in range(1,n) :
    arr.append(arr[i-1] + arr[i])

print(arr[n])
