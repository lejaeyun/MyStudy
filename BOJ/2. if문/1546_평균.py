#https://www.acmicpc.net/problem/1546
import sys
input = sys.stdin.readline


def main() :
    N = int(input())
    M = list(map(int, input().split()))
    m = max(M)
    for i in range(len(M)) :
        M[i] = (M[i]/m) * 100
    avg = (sum(M) / len(M))
    print(avg)

main()
