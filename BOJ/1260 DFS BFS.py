#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def DFS(array, vertex) :
    queue = list()
    visit = list()
    queue.extend(array[vertex])
    visit.append(vertex)
    print(vertex, end = " ")
    while queue :
        nxt = queue.pop(0)
        if nxt not in visit :
            print(nxt, end = " ")
            visit.append(nxt)
            queue = array[nxt] + queue
    print()

def BFS(array, vertex) :
    queue = list()
    visit = list()
    queue.extend(array[vertex])
    visit.append(vertex)
    print(vertex, end = " ")
    while queue :
        nxt = queue.pop(0)
        if nxt not in visit :
            print(nxt, end = " ")
            visit.append(nxt)
            queue.extend(array[nxt])
    print()


def main() :
    N,M,V = map(int,input().split())
    arr = [[] for _ in range(N + 1)]

    for i in range(M) :
        v,e = map(int,input().split())
        arr[v].append(e)
        arr[e].append(v)
        
    for i in range(N) :
        arr[i+1].sort()

    DFS(arr, V)
    BFS(arr, V)
        
main()
