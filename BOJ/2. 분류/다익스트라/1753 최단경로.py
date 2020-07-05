import sys
input = sys.stdin.readline

def dijkstra(v_start, arr) :
    INF = sys.maxsize
    length = len(arr)
    nvertex = v_start-1
    visit = [False] * length
    Result = [INF] * length
    Result[nvertex] = 0
    visit[nvertex] = True

    for _ in range(length-1) :
        mini = INF

        for i in range(length) :
            if i in arr[nvertex].keys() :
                Result[i] = min( Result[i], Result[nvertex] + arr[nvertex][i] )

        for i in range(length) :
            if visit[i] == False and Result[i] < mini :
                mini = Result[i];
                vnear = i
                
        visit[vnear] = True

        for i in range(length) :
            Result[vnear] = min( Result[vnear], Result[nvertex] + mini )

        nvertex = vnear
 
    return Result

def main() :
    INF = sys.maxsize
    V,E = map(int, input().split())
    start = int(input())
    arr = [{} for _ in range(V)]
    
    for _ in range(E) :
        u,v,w = map(int, input().split())
        if v-1 not in arr[u-1].keys() :
            arr[u-1][v-1] = w
        else :
            if arr[u-1][v-1] > w :
                arr[u-1][v-1] = w
                
    result = dijkstra(start, arr)

    for i in result :
        print(i if i != INF else "INF")

    return

main()
