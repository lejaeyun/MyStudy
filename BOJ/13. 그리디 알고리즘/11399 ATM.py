#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    Sum = 0
    for i in range(N) :
        Sum = Sum + arr[i] * (N - i)
    print(Sum)
        
main()
