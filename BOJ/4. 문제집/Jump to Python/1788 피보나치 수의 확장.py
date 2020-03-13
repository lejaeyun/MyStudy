import sys
input = sys.stdin.readline

n = int(input())

if n >= 0 :
    arr = [0,1]
    for i in range(1,n) :
        arr.append(arr[i-1]+arr[i]%1000000000)
    if arr[n] == 0 :
        print(0)
    elif arr[n] > 0 :
        print(1)
    elif arr[n] < 0 :
        print(-1)
    print(abs(arr[n])%1000000000)
else :
    arr = [0, 1]
    abs_n = abs(n)
    for i in range(1,abs_n) :
        num = arr[i-1]-arr[i]
        if num < 0 :
            arr.append(-(abs(num)%1000000000))
        else :
            arr.append(num%1000000000)
    if arr[abs_n] == 0 :
        print(0)
    elif arr[abs_n] > 0 :
        print(1)
    elif arr[abs_n] < 0 :
        print(-1)
    print(abs(arr[abs_n])%1000000000)
