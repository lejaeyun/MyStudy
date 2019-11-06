#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    n = int(input())
    arr = list()
    s_arr = list()
    for _ in range(n) :
        arr.append(list(map(int, input().split())))
        s_arr.append([0 for i in range(2**_)])
    
    for c in range(n) :
        if c == 0 :
            s_arr[0] = arr[0]
            continue
        for r in range(0, c) :
            s_arr[c][(2 * r)] = s_arr[c-1][r] + arr[c][r]
            s_arr[c][(2 * r) + 1] = s_arr[c-1][r] + arr[c][r+1]
            
    print(s_arr)
    return 0;
        
main()
