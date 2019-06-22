#https://www.acmicpc.net/problem/4344
import sys
input = sys.stdin.readline


def main() :
    N = int(input())
    for _ in range(N) :
        M = list(map(int, input().split()))
        M.pop(0)
        avg = sum(M)/len(M)
        result = 0
        for i in M :
            if i > avg :
                result += 1
        print(format(result/len(M) * 100, ".3f"), end = "%\n")

main()
