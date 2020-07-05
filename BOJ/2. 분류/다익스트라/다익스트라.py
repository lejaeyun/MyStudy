import sys

#dijkstra algorithm 4.3을 약간 수정하였다.
def dijkstra(v_start, arr) :
    # 무한대를 지칭하는 INF 정의
    INF = sys.maxsize
    # 총 vertex의 개수 Algorithm 4.3에선 n과 대치
    length = len(arr)
    # 현재 vertex이다
    nvertex = v_start-1
    # 방문한 vertex 저장
    visit = [False] * length
    # 최단거리를 저장하는 배열, 출발점을 0으로 둔다
    Result = [INF] * length
    Result[nvertex] = 0
    visit[nvertex] = True

    
    print("초기 결과표 :", Result)
    print()
    for _ in range(length-1) :
        mini = INF
        # 현재 좌표에서 갈 수 있는 vertex에 대해 최단거리를 Result에 대입한다.
        for i in range(length) :
            Result[i] = min( Result[i], Result[nvertex] + arr[nvertex][i] )

        # 방문하지 않은 노드 중 다음 방문할 vertex와 minimum을 정한다.
        for i in range(length) :
            if visit[i] == False and Result[i] < mini :
                mini = Result[i];
                vnear = i
        # 방문 체크
        visit[vnear] = True

        # 최단거리 최신화
        for i in range(length) :
            Result[vnear] = min( Result[vnear], Result[nvertex] + mini )
        # 현재 vertex 업데이트
        nvertex = vnear
        print(_+1,"번째 선택된 vertex :", nvertex)
        print(_+1,"번째 진행한 결과표 :", Result)
        print()
 
    return Result

def main() :
    INF = sys.maxsize
    arr = [[INF,INF,6,3,INF], \
           [3,INF,INF,INF,INF], \
           [INF,INF,INF,2,INF], \
           [INF,1,1,INF,INF], \
           [INF,4,INF,2,INF], \
           ]
    
    print(dijkstra(5, arr))

    return

main()
