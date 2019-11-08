#https://www.acmicpc.net/problem/1712
import sys
input = sys.stdin.readline

def main() :
    A,B,C = map(int,input().split())
    if B >= C :
        print("-1")
    else :
        s = (A // (C-B))+1
        print(s)
        
main()
