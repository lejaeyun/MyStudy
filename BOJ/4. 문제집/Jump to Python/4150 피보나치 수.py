import sys
input = sys.stdin.readline

n = int(input())
arr = [1,1,1]
for i in range(2,n) :
    arr.append(arr[i-1] + arr[i])
    
print(arr[n])
