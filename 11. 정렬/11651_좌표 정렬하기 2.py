#https://www.acmicpc.net/problem/11651
import sys
input = sys.stdin.readline

def main() :
    N = int(input())
    pos = []
    for i in range(N) :
        A,B = map(int, input().split())
        pos.append([B,A])

    pos.sort()
    for i in pos :
        print(i[1],i[0])
    return 0;
        
main()
