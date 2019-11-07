#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def main() :
    d = dict()
    N,M = map(int, input().split())
    for i in range(N) :
        s = input().split()[0]
        d[s] = i+1
        
    a = list(d.keys())
    
    for _ in range(M) :
        i = input()
        if i[0] >= '0' and i[0] <= '9' :
            i = int(i)
            print(a[i-1])
        else :
            print(d[i.split()[0]])
        
main()
