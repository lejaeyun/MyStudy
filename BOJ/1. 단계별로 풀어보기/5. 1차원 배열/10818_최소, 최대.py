#https://www.acmicpc.net/problem/10818
import sys
input = sys.stdin.readline

def main() :
    N = int(input())
    arr = list(map(int, input().split()))
    print(min(arr), max(arr))
        
main()
