#https://www.acmicpc.net/problem/10952
import sys
input = sys.stdin.readline

def main() :
    while True :
        A,B = map(int, input().split())
        if A == B and A == 0 :
            break
        print(A+B)
        
main()
