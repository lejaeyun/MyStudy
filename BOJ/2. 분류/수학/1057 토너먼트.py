#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    N, K, I = map(int, input().split())
    arr = [[i] for i in range(1, N+1)]
    cnt = 0
    while True :
        N = len(arr)//2
        tmparr = list()
        
        for i in range(N) :
            tmparr.append(arr[2*i] + arr[2*i+1])
        if len(arr) % 2 == 1 :
            tmparr.append(arr[-1])
        arr = tmparr
        cnt = cnt + 1
        for l in arr :
            if K in l and I in l :
                print(cnt)
                return
        
main()
