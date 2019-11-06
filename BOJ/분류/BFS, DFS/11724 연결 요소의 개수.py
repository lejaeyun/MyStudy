#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def bfs(dic, visit, n) :
    stack = list()
    num = 0
    if not visit[n] :
        stack.extend(dic[n])
        num = 1

    while stack :
        nxt = stack.pop()
        if not visit[nxt] :
            visit[nxt] = 1
            stack.extend(dic[nxt])
            
    return num, visit


def main() :
    N, M = map(int, input().split())
    arr = dict()
    for i in range(N+1) :
        arr[i] = []
        
    for _ in range(M) :
        u,v = map(int,input().split())
        arr[u].append(v)
        arr[v].append(u)
        
    num = 0
    visit = [0 for _ in range(N+1)]
    for i in range(1, N+1) :
        tnum, visit = bfs(arr, visit, i)
        num += tnum
    print(num)
        
main()
