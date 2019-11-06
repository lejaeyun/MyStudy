#https://www.acmicpc.net/problem/
import sys
input = sys.stdin.readline

def bfs(arr, x, y,M,N) :
    stack = list()
    stack.append([x,y])
    num = 0
    while stack :
        nxt = stack.pop()
        x, y = nxt[0], nxt[1]
        if arr[y][x] == 0 :
            arr[y][x] = 1
            num += 1
            
            if inorout(x+1,y,M,N) :
                if arr[y][x+1] == 0 :
                    stack.append([x+1,y])
                
            if inorout(x-1,y,M,N) :
                if arr[y][x-1] == 0 :
                    stack.append([x-1,y])
                
            if inorout(x,y+1,M,N) :
                if arr[y+1][x] == 0 :
                    stack.append([x,y+1])
                
            if inorout(x,y-1,M,N) :
                if arr[y-1][x] == 0 :
                    stack.append([x,y-1])
                    
    return arr, num

def inorout(x, y , M, N) :
    if x >= 0 and x < N :
        if y >= 0 and y < M :
            return 1
    return 0

def draw(arr, sx, sy, ex, ey) :
    for i in range(sx, ex) :
        for j in range(sy, ey) :
            arr[j][i] = 1
    return arr

def main() :
    M,N,K = map(int, input().split())
    arr = [[0 for _ in range(N)] for __ in range(M)]
    resultarr = list()

    for _ in range(K) :
        sx, sy ,ex ,ey = map(int, input().split())
        arr = draw(arr, sx, sy, ex, ey)

    for i in range(N) :
        for j in range(M) :
            if arr[j][i] == 0 :
                arr, tnum = bfs(arr, i,j,M,N)
                if tnum : resultarr.append(tnum)
                
    print(len(resultarr))
    resultarr.sort()
    for l in resultarr :
        print(l, end = " ")
    
    return 0;
        
main()
