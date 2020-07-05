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
    N,M,X = map(int, input().split())
    arr = [{} for _ in range(N)]
    for _ in range(M) :
        u,v,w = map(int, input().split())
        arr[u-1][v-1] = w
        
    m = 0
    result = []
    for i in range(N) :
        result.append(dijkstra(i+1, arr))
        
    for i in range(len(result)) :
        for j in range(len(result)) :
            if i == j : continue
            if m < result[i][j] + result[j][i] :
                m = result[i][j] + result[j][i]
            
    print(m)

main()
