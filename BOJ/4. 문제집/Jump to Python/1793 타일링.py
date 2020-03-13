import sys
input = sys.stdin.readline
arr = [1,1]
for i in range(1,251) :
    arr.append(arr[i] + arr[i-1]*2)
try :
    while True:
        n = int(input())
        print(arr[n])
except :
    pass
