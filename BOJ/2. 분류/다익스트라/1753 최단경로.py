#https://www.acmicpc.net/problem/1753
import sys
input = sys.stdin.readline
from collections import deque
import heapq

INF = sys.maxsize

def dijkstra(mydict,start,v) :
    stack = list()
    for tmpw,tmpv in mydict[start] :
        heapq.heappush(stack, [tmpw,tmpv])
        
    result = list()
    for _ in range(v+1) :
        result.append(INF)
    result[start] = 0

    minnxt = start
    while stack:
        minimum = INF
        tmpnxt = result[minnxt]
        while stack:
            tmp = heapq.heappop(stack)
            nxt = tmp[1]
            w = tmp[0] + tmpnxt
            if w < minimum :
                minimum = w
                minnxt = nxt
            
            if w < result[nxt] :
                result[nxt] = w
                
        for tmpw,tmpv in mydict[minnxt] :
            heapq.heappush(stack, [tmpw,tmpv])
            

    return result

def main() :
        V,E = map(int, input().split())
        Start = int(input())
        mydict = dict()
        for i in range(1,V+1) :
            mydict[i] = list()

        for _ in range(E) :
            u,v,w = map(int,input().split())
            mydict[u].append([w,v])
        
        result = dijkstra(mydict, Start,V)
        

        for v in range(1, V+1) :
            if result[v] == INF :
                print("INF")
                continue
            print(result[v])

        return 0
main()
