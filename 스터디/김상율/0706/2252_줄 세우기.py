#https://www.acmicpc.net/problem/2252
import sys
input = sys.stdin.readline

def main() :
    N,M = map(int,input().split())
    line = dict()
    n = [-1 for _ in range(N+1)]
    lst = []
    idx = 0
    
    for i in range(N) :
        line[i+1] = []
    
    for i in range(M) :
        A,B = map(int, input().split())
        if n[A] == n[B] and n[A] == -1 :
            lst.append(B)
            n[A],n[B] = idx, idx
            idx = idx + 1
        else :
            if n[A] != -1 :
                n[B] = n[A]
            else :
                n[A] = n[B]
            
        line[B].append(A)
        lst[idx - 1] = B
        
    return 0;
        
main()
