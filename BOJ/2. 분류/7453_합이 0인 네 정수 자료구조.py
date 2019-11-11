#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline
import itertools

def main() :
    result = 0
    d = {0 : [], 1 : [], 2 : [], 3 : []}
    num = int(input())
    narr = [i for i in range(num)]
    
    for _ in range(num) :
        s = list(map(int, input().split()))
        d[0].append(s[0])
        d[1].append(s[1])
        d[2].append(s[2])
        d[3].append(s[3])
        
    ll = list(itertools.product(narr,repeat = 4))
    for i,j,k,l in ll :
        if (d[0][i] + d[1][j] + d[2][k] + d[3][l]) == 0 :
            result += 1
        
        
    print(result)
        
main()
