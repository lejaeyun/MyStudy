import sys
input = sys.stdin.readline

arr = [1,1]
n = int(input())
for i in range(1,n) :
    arr.append((arr[i-1]*2 + arr[i])%10007)

print(arr[n]%10007)
