#https://www.acmicpc.net/problem/11650
import sys
input = sys.stdin.readline

def main() :
    N = int(input())
    pos = []
    for i in range(N) :
        pos.append(list(map(int, input().split())))

    pos.sort()
    for i in pos :
        print(i[0],i[1])
    return 0;
        
main()
