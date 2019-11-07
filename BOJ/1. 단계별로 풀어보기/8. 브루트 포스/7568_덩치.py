#https://www.acmicpc.net/problem/7568
import sys
input = sys.stdin.readline

def main() :
    N = int(input())
    R = list()
    dc = list()
    for _ in range(N) :
        dc.append(list(map(int, input().split())))

    for i in range(N) :
        rank = 1
        for j in range(N) :
            if i == j :
                continue
            if dc[i][0] < dc[j][0] and dc[i][1] < dc[j][1] :
                rank = rank + 1
        R.append(rank)
        
    print(*R)
        
        
main()
