#https://www.acmicpc.net/problem/2798
import sys
input = sys.stdin.readline
import itertools

def main() :
    N,M = map(int, input().split())
    l = list(map(int, input().split()))
    l = list(itertools.combinations(l, 3))
    r = -1
    
    for i in l :
        s = sum(i)
        if s <= M :
            r = max(r, s)
            
    print(r)
        
main()
