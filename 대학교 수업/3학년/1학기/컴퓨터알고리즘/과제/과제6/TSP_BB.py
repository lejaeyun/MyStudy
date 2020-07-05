import heapq
import sys
import copy
INF = sys.maxsize
'''
# 문제 8번
# 책에서 설명한 대로 Bound를 반환한다.
def bound(route, path) :
    _bound = list()
    for tmplist in route :
        tmparray = list()
        for i in range(len(tmplist)) :
            if i not in path and tmplist[i] != 0 :
                tmparray.append(tmplist[i])
        _bound.append(min(tmparray))
    return sum(_bound)
'''
# 문제 11번
# 연결되지 않은 부분을 INF로 정의
# 리스트가 빈 경우 0을 append
# INF는 고려 X
def bound(route, path) :
    _bound = list()
    for tmplist in route :
        tmparray = list()
        for i in range(len(tmplist)) :
            if i not in path and tmplist[i] != 0 and tmplist[i] != INF :
                tmparray.append(tmplist[i])
        if tmparray : _bound.append(min(tmparray))
        else : _bound.append(0)
    return sum(_bound)

# Travel algorithm
# heap (bound == boundsum, path, length)
def travel(route,v_start) :
    heap = list()
    len_route = len(route)
    path = [v_start]
    boundsum = bound(route, path)
    heapq.heappush(heap,(boundsum, path, 0))
    minlength = INF
    while heap :
        nxt = heapq.heappop(heap)
        print("nowindex : " ,nxt[-1-1][-1])
        for i in range(1, len_route) :
            # copy된 값 에러를 없애기 위해 deepcopy 사용.
            boundsum, path, length = tuple(copy.deepcopy(nxt))
            if i in path : continue
            # path, length 갱신
            path.append(i)
            length = length + route[path[-1-1]][path[-1]]
            #INF일 경우 continue
            if route[path[-1-1]][path[-1]] == INF : continue
            # 마지막 vertex만 남았을 때
            if len(path) == len_route-1 :
                v_last = 0
                for i in range(len_route) :
                    if i not in path :
                        v_last = i
                        length += route[path[-1]][v_last]
                        path.append(i)
                path.append(0)
                length += route[v_last][0]
                if length < minlength :
                    minlength = length
                    result_tour = path
                    print("minlength Update : ", path)
            else :
                boundsum = bound(route, path)
            # bound가 minlength보다 작을때 (방문해볼 가치가 있을 때) insert
            if boundsum < minlength :
                print("inserting : ",(boundsum, path,length))
                heapq.heappush(heap, (boundsum, path, length))
    print("heap is empty")
    return path, minlength


def main() :
    route = [ [INF,5,8,INF, INF, INF, INF, INF],
              [INF, INF, 4, INF, 4, INF, INF, INF],
              [INF, INF, INF, 2, INF, INF, 5, INF],
              [INF, INF, INF, INF, INF, INF, INF, 7],
              [1, INF, INF, INF, INF, INF, INF, INF],
              [INF, 6, INF, INF, 2, INF, INF, INF],
              [INF, INF, INF, INF, INF, 8, INF, INF],
              [INF, INF, INF, INF, INF, 5, 4, INF]
              ]
    
    for i in range(len(route)) :
        route[i][i] = 0
        
    length = 0
    result = travel(route,0)
    for i in range(len(result[0])) :
        result[0][i] += 1
    print("result path : ", result[0])
    print("minlength : ", result[1])

main()
