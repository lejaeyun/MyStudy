#https://www.acmicpc.net/problem/1110
import sys
input = sys.stdin.readline


def main() :
    N = int(input())
    result = 0
    a = N
    while True :
        b = a % 10
        a = a // 10
        result = result + 1
        a = b * 10 + ((a + b) % 10)
        
        if a == N :
            break
    print(result)


main()
