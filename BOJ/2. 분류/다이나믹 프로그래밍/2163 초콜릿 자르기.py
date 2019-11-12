#https://www.acmicpc.net/problem/2163
import sys
input = sys.stdin.readline

def main() :
    N,M = map(int, input().split())
    result = (M-1) + (M)*(N-1)
    print(result)
    return 0;
        
main()
