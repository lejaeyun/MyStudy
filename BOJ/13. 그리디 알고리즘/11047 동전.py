#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    N, K = map(int, input().split())
    coin_arr = list()
    for i in range(N) :
        coin_arr.append(int(input()))

    coin = 0
    while K > 0 :
        for i in range(N-1, -1, -1) :
            if K >= coin_arr[i] :
                coin += K // coin_arr[i]
                K = K - (K // coin_arr[i]) * coin_arr[i]
                break
            else :
                coin_arr.pop(i)
                N -= 1
    print(coin)
        
main()
