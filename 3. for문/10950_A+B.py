#https://www.acmicpc.net/problem/10950
import sys
input = sys.stdin.readline

def main() :
    N = int(input())
    for _ in range(N) :
        A,B = map(int, input().split())
        print(A+B)
    
main()
