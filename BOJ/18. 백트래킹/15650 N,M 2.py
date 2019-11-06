#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline
import itertools

def main() :
    N,M = map(int, input().split())
    arr = [i for i in range(1, N + 1)]
    if M == 1 :
        for l in arr :
            print(l)
    else :
        arr = list(itertools.combinations(arr, M))
        arr.sort()
        for l in arr :
            ll = str(l)[1:len(str(l))-1].split(",")
            for i in range(len(ll)) :
                print(ll[i], end = "")
            print()
        
main()
