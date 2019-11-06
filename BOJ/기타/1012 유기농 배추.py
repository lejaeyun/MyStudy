#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline
def find_cabbage(array, M, N) :
    earthworm = 0
    visit = list()
    start = 0
    while start < M*N :
        x,y = start % M, start // M
        if array[y][x] == 1 :
            if start not in visit :
                visit.extend( BFS(array,M,N,start) )
                earthworm += 1
        start += 1
            
    return earthworm

def BFS(array, M, N, start) :
    queue = list()
    visit = list()
    queue.append(start)
    while queue :
        nxt = queue.pop(0)
        x,y = nxt % M, nxt // M
        if nxt not in visit :
            visit.append(nxt)
            try :
                if array[y][x + 1] == 1 :
                    queue.append(nxt + 1)
            except :
                pass
            try :
                if array[y][x - 1] == 1 and x != 0 :
                    queue.append(nxt - 1)
            except :
                pass
            try :
                if array[y+1][x] == 1 :
                    queue.append(nxt + M)
            except :
                pass
            try :
                if array[y-1][x] == 1 and y != 0 :
                    queue.append(nxt - M)
            except :
                pass
    return visit

def main() :
    for _ in range(int(input())) :
        M,N,K = map(int,input().split())
        arr = [[0 for _ in range(M)] for __ in range(N)]
        
        for _ in range(K) :
            x,y = map(int, input().split())
            arr[y][x] = 1
            
        print(find_cabbage(arr, M, N))
        
main()
